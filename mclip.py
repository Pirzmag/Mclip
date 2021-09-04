#!/usr/bin/env python3
# mclip.py - a multi-clipboard utility

import sys
import pyperclip

TEXT = {'agree': 'Yes, we can do this',
        'disagree': 'No way to do this hombre',
        'tea': 'Bring me some tea bro',
        }

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text to clipboard')
    sys.exit()

keyphrase = sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for '{keyphrase}' copied to clipboard")
else:
    print(f"Text for '{keyphrase}' is not available")
