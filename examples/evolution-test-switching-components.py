#!/usr/bin/env python
# Dogtail demo script
__author__ = 'David Malcolm <dmalcolm@redhat.com>'

# Test repeatedly switching between evolution components
#
# Assumes evolution is configured and is running
#

import dogtail.tree

evo = dogtail.tree.root.application('evolution')

while True:
	for compName in ['Mail', 'Contacts', 'Calendars', 'Tasks']:
		evo.menu('View').menu('Window').menuItem(compName).click()