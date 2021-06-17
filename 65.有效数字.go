type State int
type Input int

const (
	STATE_INIT State = iota
	STATE_SIGN
	STATE_INTEGER
	STATE_POINT
	STATE_POINT_WITHOUT_INT
	STATE_FRACTION
	STATE_EXP
	STATE_EXP_SIGN
	STATE_EXP_INT
	STATE_REJECT
)
const (
	NUMBER Input = iota
	POINT
	EXP
	SIGN
	OTHER
)

func toInput(ch byte) Input {
	switch ch {
	case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
		return NUMBER
	case 'e', 'E':
		return EXP
	case '+', '-':
		return SIGN
	case '.':
		return POINT
	default:
		return OTHER
	}
}

func isNumber(s string) bool {
	transfer := map[State]map[Input]State{
		STATE_INIT: {
			SIGN:   STATE_SIGN,
			NUMBER: STATE_INTEGER,
			POINT:  STATE_POINT_WITHOUT_INT,
		},
		STATE_SIGN: {
			NUMBER: STATE_INTEGER,
			POINT:  STATE_POINT_WITHOUT_INT,
		},
		STATE_INTEGER: {
			NUMBER: STATE_INTEGER,
			POINT:  STATE_POINT,
			EXP:    STATE_EXP,
		},
		STATE_POINT_WITHOUT_INT: {
			NUMBER: STATE_FRACTION,
		},
		STATE_POINT: {
			NUMBER: STATE_FRACTION,
			EXP:    STATE_EXP,
		},
		STATE_FRACTION: {
			NUMBER: STATE_FRACTION,
			EXP:    STATE_EXP,
		},
		STATE_EXP: {
			NUMBER: STATE_EXP_INT,
			SIGN:   STATE_EXP_SIGN,
		},
		STATE_EXP_SIGN: {
			NUMBER: STATE_EXP_INT,
		},
		STATE_EXP_INT: {
			NUMBER: STATE_EXP_INT,
		},
	}
	state := STATE_INIT
	for i := 0; i < len(s); i++ {
		in := toInput(s[i])
		if _, ok := transfer[state][in]; !ok {
			return false
		}
		state = transfer[state][in]
	}
	return state == STATE_INTEGER || state == STATE_POINT || state == STATE_FRACTION || state == STATE_EXP_INT
}
