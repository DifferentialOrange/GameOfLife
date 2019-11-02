import sys
sys.path.insert(1, '.')
import game.field as fields

def test_dots():
	field = fields.closedField(size=(5, 5))
	field[0][0] = True
	field[1][2] = True
	field[3][2] = True
	field[4][3] = True

	ans_field = fields.closedField(size=(5, 5))

	field.NextStep()

	# All dots should die
	assert field == ans_field

	field.NextStep()

	# No dots should born
	assert field == ans_field

def test_born():
	field = fields.closedField(size=(4, 4))
	field[1][0] = True
	field[0][1] = True
	field[2][2] = True

	ans_field = fields.closedField(size=(4, 4))
	ans_field[1][1] = True

	ans2_field = fields.closedField(size=(4, 4))

	field.NextStep()

	# New dot should born, another should die
	assert field == ans_field

	field.NextStep()

	# Last dot should die
	assert field == ans2_field

def test_stay_alive():
	field = fields.closedField(size=(1, 3))
	field[0][0] = True
	field[0][1] = True
	field[0][2] = True

	ans_field = fields.closedField(size=(1, 3))
	ans_field[0][1] = True

	ans2_field = fields.closedField(size=(1, 3))

	field.NextStep()

	# Dot in the middle should remain alive
	assert field == ans_field

	field.NextStep()

	# Last dot should die
	assert field == ans2_field

def test_block():
	field = fields.closedField(size=(4, 4))
	field[1][1] = True
	field[1][2] = True
	field[2][1] = True
	field[2][2] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Block shoud remain
	assert field == ans_field

def test_corner_block():
	field = fields.closedField(size=(4, 4))
	field[0][0] = True
	field[0][1] = True
	field[1][0] = True
	field[1][1] = True

	ans_field = fields.closedField(other=field)

	field.NextStep()

	# Square shoud remain
	assert field == ans_field

def test_block_with_dot():
	field = fields.closedField(size=(4, 4))
	field[0][0] = True
	field[0][1] = True
	field[1][0] = True
	field[1][1] = True
	field[3][3] = True

	ans_field = fields.closedField(other=field)
	ans_field[3][3] = False

	field.NextStep()

	# Block shoud remain, dot should die
	assert field == ans_field
