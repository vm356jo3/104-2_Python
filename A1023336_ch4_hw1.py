#!/usr/bin/env python
# -*- coding: utf-8 -*-
name={'Mary':'Honey', 'Lynn':'Baby', 'Jannie':'Little sweetie'}
str="Honey, you are always on my mind. Your love makes me blind .When I first met you I knew it was a sign."
print u'Mary來了！'
print u'花心郎要對Mary說：'
print str.replace('Honey', name['Mary'])
print ''
print u'Mary走了，Lynn來了！'
print u'花心郎要對Lynn說：'
print str.replace('Honey', name['Lynn'])
print ''
print u'Lynn走了，Jannie來了！'
print u'花心郎要對Jannie說：'
print str.replace('Honey', name['Jannie'])