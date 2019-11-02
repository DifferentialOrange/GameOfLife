import sys
sys.path.insert(1, '.')
import rules.field as fields

def test_glider():
	field = fields.closedField(size=(8, 8))
	field[0][1] = True
	field[1][2] = True
	field[2][0] = True
	field[2][1] = True
	field[2][2] = True

	ans_field = fields.closedField(size=(8, 8))
	ans_field[1][0] = True
	ans_field[1][2] = True
	ans_field[2][1] = True
	ans_field[2][2] = True
	ans_field[3][1] = True

	ans2_field = fields.closedField(size=(8, 8))
	ans2_field[1][2] = True
	ans2_field[2][0] = True
	ans2_field[2][2] = True
	ans2_field[3][1] = True
	ans2_field[3][2] = True

	ans3_field = fields.closedField(size=(8, 8))
	ans3_field[1][1] = True
	ans3_field[2][2] = True
	ans3_field[2][3] = True
	ans3_field[3][1] = True
	ans3_field[3][2] = True

	ans4_field = fields.closedField(size=(8, 8))
	ans4_field[1][2] = True
	ans4_field[2][3] = True
	ans4_field[3][1] = True
	ans4_field[3][2] = True
	ans4_field[3][3] = True

	field.NextStep()

	# Glider moved
	assert field == ans_field

	field.NextStep()

	# Glider moved
	assert field == ans2_field

	field.NextStep()

	# Glider moved
	assert field == ans3_field

	field.NextStep()

	# Glider moved, returned to the initial form
	assert field == ans4_field
