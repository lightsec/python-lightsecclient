"""
Created on 13/12/2014

@author: Aitor Gomez Goiri <aitor.gomez@deusto.es>
"""


import socket
import binascii
from abc import ABCMeta, abstractmethod
#from http.client import HTTPConnection
from httplib import HTTPConnection
from lightsec.helpers import UserHelper


class AbstractLoginManager(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self, *args, **kwargs):
        """
        :return: Dictionary with id, kenc, kauth, user id, a, init_time and exp_time.
        """
        pass


class LightSecHTTPConnection(HTTPConnection):

    def __init__(self, host, port=None, strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None,
                 login_manager=None):
        super(LightSecHTTPConnection, self).__init__(host, port, strict, timeout, source_address)
        self.login_manager = login_manager

    def _set_user_helper(self):
        # self.user = UserHelper(SENSOR_ID, stuff["kenc"], AESCTRCipher,
        #                        stuff["kauth"], SHA256Hash, self.USER_ID,
        #                        stuff["a"], stuff["init_time"], stuff["exp_time"])
        pass

    def _get_user_helper(self):
        pass

    def sec_request(self, method, url, body=None, headers={}):
        """Send a complete request to the server."""
        # params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
        enc_body = binascii.hexlify(self._get_user_helper().encrypt(body)) if body else None
        self._send_request(method, url, enc_body, headers)
