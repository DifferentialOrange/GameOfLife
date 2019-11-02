import sys
sys.path.insert(1, '.')
import game.field as fields

def test_blinker():
	field = fields.closedField(size=(4, 4))
	field[1][1] = True
	field[1][2] = True
	field[1][3] = True

	ans_field = fields.closedField(other=field)
	ans_field[1][1] = False
	ans_field[1][3] = False
	ans_field[0][2] = True
	ans_field[2][2] = True

	ans2_field = fields.closedField(other=field)

	ans3_field = fields.closedField(other=ans_field)

	field.NextStep()

	# Figure blinked
	assert field == ans_field

	field.NextStep()

	# Blinking is periodical
	assert field == ans2_field

	field.NextStep()

	# Blinking is periodical
	assert field == ans3_field

def test_beacon():
	field = fields.closedField(size=(5, 5))
	field[1][1] = True
	field[1][2] = True
	field[2][1] = True

	field[3][4] = True
	field[4][3] = True
	field[4][4] = True

	ans_field = fields.closedField(other=field)
	ans_field[2][2] = True
	ans_field[3][3] = True

	ans2_field = fields.closedField(other=field)

	ans3_field = fields.closedField(other=ans_field)

	field.NextStep()

	# Figure blinked
	assert field == ans_field

	field.NextStep()

	# Blinking is periodical
	assert field == ans2_field

	field.NextStep()

	# Blinking is periodical
	assert field == ans3_field
