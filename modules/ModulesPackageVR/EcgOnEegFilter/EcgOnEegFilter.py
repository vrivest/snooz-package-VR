"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    EcgOnEegFilter
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug # type: ignore
from commons.NodeInputException import NodeInputException # type: ignore
from commons.NodeRuntimeException import NodeRuntimeException # type: ignore
import numpy as np
import math
from scipy.signal import find_peaks
from scipy.signal import detrend


DEBUG = False

class EcgOnEegFilter(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        eeg_signals: TODO TYPE
            TODO DESCRIPTION
        ecg_signal: TODO TYPE
            TODO DESCRIPTION
        filename: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        corrected_signals: TODO TYPE
            TODO DESCRIPTION
        
    """

    def fenetres_ondes_R(self, nb_R_waves, temps_fenetre, vecteur_indices_ondes_R_ECG, fs_ECG, fs_EEG):

        intervalle = math.ceil( ((temps_fenetre/2)*fs_ECG) * (fs_EEG/fs_ECG) )
        #initialisation de la matrice avec des 0 partout
        mat_indices_debut_fin_fenetres_ondes_R = np.zeros((nb_R_waves, 2), dtype = int)
        #indices de début (1ere colonne)
        mat_indices_debut_fin_fenetres_ondes_R[:, 0] = np.floor(vecteur_indices_ondes_R_ECG*(fs_EEG/fs_ECG)) - intervalle
        #indices de fin (2e colonne)
        mat_indices_debut_fin_fenetres_ondes_R[:, 1] = np.floor(vecteur_indices_ondes_R_ECG*(fs_EEG/fs_ECG)) + intervalle

        return mat_indices_debut_fin_fenetres_ondes_R


    def plages_EEG_a_filtrer(self, nb_R_waves, mat_idx_debut_fin_fenetres):
       
        fenetres_idx = np.zeros((nb_R_waves, (mat_idx_debut_fin_fenetres[0, 1] - mat_idx_debut_fin_fenetres[0, 0] + 1)), dtype = int) # Initialisation de la matrice avec des 0
        
        Vecteur_idx_EEG_a_filtrer = np.zeros(((mat_idx_debut_fin_fenetres[0, 1] - mat_idx_debut_fin_fenetres[0, 0] + 1)*nb_R_waves), dtype = int)# Initialisation de la matrice avec des 0

        for i in range(0, nb_R_waves, 1):
           fenetres_idx[i,:] = np.arange(mat_idx_debut_fin_fenetres[i,0], mat_idx_debut_fin_fenetres[i,1] +1)

        Vecteur_idx_EEG_a_filtrer = fenetres_idx.reshape(1, -1).flatten()
        
        return Vecteur_idx_EEG_a_filtrer
    

    def __init__(self, **kwargs):
        """ Initialize module EcgOnEegFilter """
        super().__init__(**kwargs)
        if DEBUG: print('EcgOnEegFilter.__init__')

        # Input plugs
        InputPlug('eeg_signals',self)
        InputPlug('ecg_signal',self)
        InputPlug('filename',self)
        

        # Output plugs
        OutputPlug('corrected_signals',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    
 

    def compute(self, eeg_signals,ecg_signal,filename):
       
        fs_ecg = ecg_signal[0].sample_rate
        fs_eeg = eeg_signals[0].sample_rate

        Neeg = len(eeg_signals)

        Nech_ecg = ecg_signal[0].samples.size
        Nech_eeg = eeg_signals[0].samples.size

        ECG = np.zeros ((Nech_ecg), dtype=float)
        ECG = ecg_signal[0].samples

        EEG = np.zeros((Neeg, Nech_eeg), dtype = float)
        
        for i in range(0, Neeg, 1):
            EEG[i, :] = eeg_signals[i].samples

        EEG = detrend(EEG, type='linear')
        ECG = detrend(ECG, type='linear')
        max_ECG = np.max(ecg_signal[0].samples)

        #Détection des pics QRS et création d'un vecteur d'indices des pics QRS 
        peaks_idx, properties = find_peaks(ECG, height=(0.75*max_ECG))
        
        nb_ondes_R = peaks_idx.size
        grandeur_fenetres = 0.2
        
        mat_fenetres_ondes_R_idx = self.fenetres_ondes_R(nb_ondes_R, grandeur_fenetres, peaks_idx, fs_ecg, fs_eeg)
        
        Vecteur_idx_filtrage_canaux_EEG = self.plages_EEG_a_filtrer(nb_ondes_R, mat_fenetres_ondes_R_idx)

        donnees_EEG_corrompues_cardio = EEG[:, Vecteur_idx_filtrage_canaux_EEG]

        #########################      Conception du FILTRE     ###############################

        P = np.dot (donnees_EEG_corrompues_cardio, donnees_EEG_corrompues_cardio.T)
        U, _, _ = np.linalg.svd(P)
        U1 = np.array([U[:, 0]]).T

        Cardio_isole = np.dot(U1, U1.T)
        ID = np.eye(len(Cardio_isole))
        Filtre = ID - Cardio_isole

        EEG_clean = np.dot(Filtre, EEG)

        for i in range(0, Neeg, 1):
            eeg_signals[i].samples = EEG_clean[i]
            eeg_signals[i].is_modified = True
        ########################################################################################

        """
        TODO DESCRIPTION

        Parameters
        ----------
            eeg_signals: TODO TYPE
                TODO DESCRIPTION
            ecg_signal: TODO TYPE
                TODO DESCRIPTION
            filename: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            corrected_signals: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Code examples

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        # raise NodeInputException(self.identifier, "my_input", \
        #        f"EcgOnEegFilter this input is wrong.")

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This will usually be a user error, a file that can't be read due to security reason,
        # a parameter that is out of bound, etc. This exception will stop and skip the current
        # process but will not stop the followin iterations if a master node is not done.
        # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
        # to the user.
        #
        # Set the iteration_identifier if this module is a master node.
        # This will be used to identify the problematic iteration if a runtime exception occurs
        # in any module during this process. For example, a master node that reads one file at a 
        # could set the identifier to the name of the file.
        # self.iteration_identifier = current_filename
        #
        # Iteration count and counter are used to show a progress bar in percent.
        # Update these when creating a master node to properly show the progress 
        # for each iteration. This is optional and can be ignored but it's a good practice
        # to do for your users.
        #self.iteration_count = the total amout of iteration to make
        #self.iteration_counter = the current iteration number

        #
        # Raise the runtime exception
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        #
        #

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'corrected_signals': eeg_signals
        }