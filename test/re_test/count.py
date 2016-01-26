__author__ = 'wangp11'

OUT = """
LOGICAL UNIT NUMBER 40
Name:  test_import_volume_20141023233901
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 37
Name:  test_import_volume_20141023231903
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 36
Name:  test_import_volume_20141023231856
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 35
Name:  test_import_volume_20141023230949
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 34
Name:  test_import_volume_20141023230940
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 33
Name:  test_import_volume_20141023220442
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 32
Name:  test_import_volume_20141023220434
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 30
Name:  test_import_volume_20141022031511
Pool Name:  Pool_1

LOGICAL UNIT NUMBER 28
Name:  test_import_volume_20141022031504
Pool Name:  Pool_1
"""

pool_name = 'Pool_1'
import re
x = re.findall('Pool Name:\s+' + pool_name, OUT)

print len(x)
