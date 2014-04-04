"""
A file to keep all the horrible test output strings from making the test cases any
more difficult to read.

Peruse at your own risk...
"""

TO_STR_SIMPLE = "//...\n|___ u1//...\n|___ u2//...\n|___ //one/...\n|___ //two/...\n"

TO_DICT_USER_PATH_ALPHABET_ORDERED = \
    {'AC//...':
        {'children': ['ACu1//...', 'ACu2//...', {'AC//one/...':
            {'children': ['ACu1//one/...', 'ACu2//one/...', {'//one/blue/...':
                {'children': ['u1//one/blue/...', 'u2//one/blue/...']}}, {'AC//one/red/...':
                    {'children': ['ACu1//one/red/...', 'u2//one/red/...', '//one/red/new/...',
                        {'//one/red/old/...':
                            {'children':
                                ['u1//one/red/old/...', 'u2//one/red/old/...']}}]}}]}},
                        {'//two/...':
                            {'children': ['u1//two/...', 'u2//two/...', {'//two/black/...':
                                {'children': ['u1//two/black/...', 'u2//two/black/...']}},
                                    {'//two/blue/...':
                                        {'children': ['u1//two/blue/...', 'u2//two/blue/...']}}]}}]}}

TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED = \
    ('{"text": "AC//...", "id": "//...", "children": [{"text": "ACu1//...", "id": "u1//...", '
     '"state": {"opened": false}}, {"text": "ACu2//...", "id": "u2//...", "state": {"opened": '
     'false}}, {"text": "AC//one/...", "id": "//one/...", "children": [{"text": "ACu1//one/...",'
     ' "id": "u1//one/...", "state": {"opened": false}}, {"text": "ACu2//one/...", "id": '
     '"u2//one/...", "state": {"opened": false}}, {"text": "//one/blue/...", "id": "//one/blue/..."'
     ', "children": [{"text": "u1//one/blue/...", "id": "u1//one/blue/...", "state": {"opened": '
     'false}}, {"text": "u2//one/blue/...", "id": "u2//one/blue/...", "state": {"opened": false}}],'
     ' "state": {"opened": false}}, {"text": "AC//one/red/...", "id": "//one/red/...", "children":'
     ' [{"text": "ACu1//one/red/...", "id": "u1//one/red/...", "state": {"opened": false}}, '
     '{"text": "u2//one/red/...", "id": "u2//one/red/...", "state": {"opened": false}}, {"text":'
     ' "//one/red/new/...", "id": "//one/red/new/...", "state": {"opened": false}}, {"text": '
     '"//one/red/old/...", "id": "//one/red/old/...", "children": [{"text": "u1//one/red/old/...",'
     ' "id": "u1//one/red/old/...", "state": {"opened": false}}, {"text": "u2//one/red/old/...", '
     '"id": "u2//one/red/old/...", "state": {"opened": false}}], "state": {"opened": false}}],'
     ' "state": {"opened": false}}], "state": {"opened": false}}, {"text": "//two/...", "id": '
     '"//two/...", "children": [{"text": "u1//two/...", "id": "u1//two/...", "state": {"opened":'
     ' false}}, {"text": "u2//two/...", "id": "u2//two/...", "state": {"opened": false}}, '
     '{"text": "//two/black/...", "id": "//two/black/...", "children": [{"text": "u1//two/black/...",'
     ' "id": "u1//two/black/...", "state": {"opened": false}}, {"text": "u2//two/black/...", "id":'
     ' "u2//two/black/...", "state": {"opened": false}}], "state": {"opened": false}}, {"text": '
     '"//two/blue/...", "id": "//two/blue/...", "children": [{"text": "u1//two/blue/...", "id":'
     ' "u1//two/blue/...", "state": {"opened": false}}, {"text": "u2//two/blue/...", "id":'
     ' "u2//two/blue/...", "state": {"opened": false}}], "state": {"opened": false}}], "state":'
     ' {"opened": false}}], "state": {"opened": false}}')

TYPED_TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED_EXPANDED = \
    ('{"text": "AC//...", "id": "//...", "children": [{"text": "ACu1//... an access", "id": '
     '"u1//...", "state": {"opened": true}}, {"text": "ACu2//... an access", "id": "u2//...", '
     '"state": {"opened": true}}, {"text": "AC//one/...", "id": "//one/...", "children": '
     '[{"text": "ACu1//one/... an access", "id": "u1//one/...", "state": {"opened": true}}, '
     '{"text": "ACu2//one/... an access", "id": "u2//one/...", "state": {"opened": true}}, '
     '{"text": "//one/blue/...", "id": "//one/blue/...", "children": [{"text": "u1//one/blue/... '
     'an access", "id": "u1//one/blue/...", "state": {"opened": true}}, {"text": "u2//one/blue/... '
     'an access", "id": "u2//one/blue/...", "state": {"opened": true}}], "state": {"opened": '
     'false}}, {"text": "AC//one/red/...", "id": "//one/red/...", "children": [{"text": '
     '"ACu1//one/red/... an access", "id": "u1//one/red/...", "state": {"opened": true}}, '
     '{"text": "u2//one/red/... an access", "id": "u2//one/red/...", "state": {"opened": true}}, '
     '{"text": "//one/red/new/...", "id": "//one/red/new/...", "state": {"opened": false}}, '
     '{"text": "//one/red/old/...", "id": "//one/red/old/...", "children": [{"text": '
     '"u1//one/red/old/... an access", "id": "u1//one/red/old/...", "state": {"opened": true}},'
     ' {"text": "u2//one/red/old/... an access", "id": "u2//one/red/old/...", "state": {"opened": '
     'true}}], "state": {"opened": false}}], "state": {"opened": false}}], "state": {"opened": '
     'false}}, {"text": "//two/...", "id": "//two/...", "children": [{"text": "u1//two/... '
     'an access", "id": "u1//two/...", "state": {"opened": true}}, {"text": "u2//two/... '
     'an access", "id": "u2//two/...", "state": {"opened": true}}, {"text": "//two/black/...", '
     '"id": "//two/black/...", "children": [{"text": "u1//two/black/... an access", "id": '
     '"u1//two/black/...", "state": {"opened": true}}, {"text": "u2//two/black/... an access", '
     '"id": "u2//two/black/...", "state": {"opened": true}}], "state": {"opened": false}}, '
     '{"text": "//two/blue/...", "id": "//two/blue/...", "children": [{"text": "u1//two/blue/... '
     'an access", "id": "u1//two/blue/...", "state": {"opened": true}}, {"text": "u2//two/blue/... '
     'an access", "id": "u2//two/blue/...", "state": {"opened": true}}], "state": {"opened": '
     'false}}], "state": {"opened": false}}], "state": {"opened": false}}')

TYPED_TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED_ACCESS_EXPANDED = \
    ('{"text": "AC//...", "id": "//...", "children": [{"text": "ACu1//... an access", "id": '
     '"u1//...", "state": {"opened": true}}, {"text": "ACu2//... an access", "id": "u2//...",'
     ' "state": {"opened": true}}, {"text": "AC//one/...", "id": "//one/...", "children": '
     '[{"text": "ACu1//one/... an access", "id": "u1//one/...", "state": {"opened": true}}, '
     '{"text": "ACu2//one/... an access", "id": "u2//one/...", "state": {"opened": true}}, '
     '{"text": "//one/blue/...", "id": "//one/blue/...", "children": [{"text": "u1//one/blue/... '
     'an access", "id": "u1//one/blue/...", "state": {"opened": true}}, {"text": "u2//one/blue/...'
     ' an access", "id": "u2//one/blue/...", "state": {"opened": true}}], "state": {"opened": '
     'true}}, {"text": "AC//one/red/...", "id": "//one/red/...", "children": [{"text": '
     '"ACu1//one/red/... an access", "id": "u1//one/red/...", "state": {"opened": true}}, '
     '{"text": "u2//one/red/... an access", "id": "u2//one/red/...", "state": {"opened": true}},'
     ' {"text": "//one/red/new/...", "id": "//one/red/new/...", "state": {"opened": true}}, '
     '{"text": "//one/red/old/...", "id": "//one/red/old/...", "children": [{"text": '
     '"u1//one/red/old/... an access", "id": "u1//one/red/old/...", "state": {"opened": true}}, '
     '{"text": "u2//one/red/old/... an access", "id": "u2//one/red/old/...", "state": {"opened": '
     'true}}], "state": {"opened": true}}], "state": {"opened": true}}], "state": {"opened": true}}, '
     '{"text": "//two/...", "id": "//two/...", "children": [{"text": "u1//two/... an access", "id": '
     '"u1//two/...", "state": {"opened": true}}, {"text": "u2//two/... an access", "id": '
     '"u2//two/...", "state": {"opened": true}}, {"text": "//two/black/...", "id": "//two/black/...",'
     ' "children": [{"text": "u1//two/black/... an access", "id": "u1//two/black/...", "state":'
     ' {"opened": true}}, {"text": "u2//two/black/... an access", "id": "u2//two/black/...", '
     '"state": {"opened": true}}], "state": {"opened": true}}, {"text": "//two/blue/...", '
     '"id": "//two/blue/...", "children": [{"text": "u1//two/blue/... an access", "id": '
     '"u1//two/blue/...", "state": {"opened": true}}, {"text": "u2//two/blue/... an access", '
     '"id": "u2//two/blue/...", "state": {"opened": true}}], "state": {"opened": true}}],'
     ' "state": {"opened": true}}], "state": {"opened": true}}')

TYPED_TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED_ACCESS = \
    ('{"text": "AC//...", "id": "//...", "children": [{"text": "ACu1//... an access", '
     '"id": "u1//...", "state": {"opened": true}}, {"text": "ACu2//... an access", '
     '"id": "u2//...", "state": {"opened": true}}, {"text": "AC//one/...", "id": '
     '"//one/...", "children": [{"text": "ACu1//one/... an access", "id": "u1//one/...", '
     '"state": {"opened": true}}, {"text": "ACu2//one/... an access", "id": "u2//one/...", '
     '"state": {"opened": true}}, {"text": "//one/blue/...", "id": "//one/blue/...", '
     '"children": [{"text": "u1//one/blue/... an access", "id": "u1//one/blue/...", '
     '"state": {"opened": true}}, {"text": "u2//one/blue/... an access", "id": '
     '"u2//one/blue/...", "state": {"opened": true}}], "state": {"opened": false}},'
     ' {"text": "AC//one/red/...", "id": "//one/red/...", "children": [{"text": '
     '"ACu1//one/red/... an access", "id": "u1//one/red/...", "state": {"opened": '
     'true}}, {"text": "u2//one/red/... an access", "id": "u2//one/red/...", '
     '"state": {"opened": true}}, {"text": "//one/red/new/...", "id": "//one/red/new/...", '
     '"state": {"opened": false}}, {"text": "//one/red/old/...", "id": "//one/red/old/..."'
     ', "children": [{"text": "u1//one/red/old/... an access", "id": "u1//one/red/old/...",'
     ' "state": {"opened": true}}, {"text": "u2//one/red/old/... an access", "id": '
     '"u2//one/red/old/...", "state": {"opened": true}}], "state": {"opened": '
     'false}}], "state": {"opened": false}}], "state": {"opened": false}}, {"text": '
     '"//two/...", "id": "//two/...", "children": [{"text": "u1//two/... an access", '
     '"id": "u1//two/...", "state": {"opened": true}}, {"text": "u2//two/... an access",'
     ' "id": "u2//two/...", "state": {"opened": true}}, {"text": "//two/black/...", '
     '"id": "//two/black/...", "children": [{"text": "u1//two/black/... an access", '
     '"id": "u1//two/black/...", "state": {"opened": true}}, {"text": "u2//two/black/...'
     ' an access", "id": "u2//two/black/...", "state": {"opened": true}}], "state": '
     '{"opened": false}}, {"text": "//two/blue/...", "id": "//two/blue/...", '
     '"children": [{"text": "u1//two/blue/... an access", "id": "u1//two/blue/...", '
     '"state": {"opened": true}}, {"text": "u2//two/blue/... an access", "id": '
     '"u2//two/blue/...", "state": {"opened": true}}], "state": {"opened": false}}], '
     '"state": {"opened": false}}], "state": {"opened": false}}')
