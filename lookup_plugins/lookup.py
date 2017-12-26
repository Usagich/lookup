from ansible.plugins.lookup import LookupBase
from os import os

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        for term in terms:
	  path = os.path.isfile(term)
	  if path:
	      display.v("Ansible stored in: " + str(term))
	  else:
	      display.v("This is magic, but here is no ansible link!")
	      term = path

        return path