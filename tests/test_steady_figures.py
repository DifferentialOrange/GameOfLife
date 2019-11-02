import sys
sys.path.insert(1, '.')
import rules.field as fields

def test_block():
	field = fields.closedField(size=(4, 4))
	field[1][1] = True
	field[1][2] = True
	field[2][1] = True
	field[2][2] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Block should remain
	assert field == ans_field

def test_three_blocks():
	field = fields.closedField(size=(8, 7))
	field[0][0] = True
	field[1][0] = True
	field[0][1] = True
	field[1][1] = True

	field[4][1] = True
	field[4][2] = True
	field[5][1] = True
	field[5][2] = True

	field[4][5] = True
	field[4][6] = True
	field[5][5] = True
	field[5][6] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Blocks should remain
	assert field == ans_field

def test_beehive():
	field = fields.closedField(size=(5, 5))
	field[2][2] = True
	field[2][3] = True
	field[3][4] = True
	field[3][1] = True
	field[4][2] = True
	field[4][3] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Beehive should remain
	assert field == ans_field

def test_loaf():
	field = fields.closedField(size=(6, 6))
	field[2][2] = True
	field[2][3] = True
	field[3][4] = True
	field[3][1] = True
	field[4][4] = True
	field[4][2] = True
	field[5][3] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Loaf should remain
	assert field == ans_field

def test_block_and_loaf():
	field = fields.closedField(size=(10, 10))
	field[2][2] = True
	field[2][3] = True
	field[3][4] = True
	field[3][1] = True
	field[4][4] = True
	field[4][2] = True
	field[5][3] = True

	field[7][5] = True
	field[7][6] = True
	field[8][5] = True
	field[8][6] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Block and loaf should remain
	assert field == ans_field
