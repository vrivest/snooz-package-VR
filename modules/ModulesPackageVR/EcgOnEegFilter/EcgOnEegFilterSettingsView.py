"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the EcgOnEegFilter plugin
"""

from qtpy import QtWidgets

from ModulesPackageVR.EcgOnEegFilter.Ui_EcgOnEegFilterSettingsView import Ui_EcgOnEegFilterSettingsView
from commons.BaseSettingsView import BaseSettingsView # type: ignore

class EcgOnEegFilterSettingsView(BaseSettingsView, Ui_EcgOnEegFilterSettingsView, QtWidgets.QWidget):
    """
        EcgOnEegFilterView set the EcgOnEegFilter settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._eeg_signals_topic = f'{self._parent_node.identifier}.eeg_signals'
        self._pub_sub_manager.subscribe(self, self._eeg_signals_topic)
        self._ecg_signal_topic = f'{self._parent_node.identifier}.ecg_signal'
        self._pub_sub_manager.subscribe(self, self._ecg_signal_topic)
        self._filename_topic = f'{self._parent_node.identifier}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._eeg_signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._ecg_signal_topic, 'ping')
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to EcgOnEegFilter
        self._pub_sub_manager.publish(self, self._eeg_signals_topic, str(self.eeg_signals_lineedit.text()))
        self._pub_sub_manager.publish(self, self._ecg_signal_topic, str(self.ecg_signal_lineedit.text()))
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._eeg_signals_topic:
            self.eeg_signals_lineedit.setText(message)
        if topic == self._ecg_signal_topic:
            self.ecg_signal_lineedit.setText(message)
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._eeg_signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._ecg_signal_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            