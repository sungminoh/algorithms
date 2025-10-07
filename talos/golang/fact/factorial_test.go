package fact

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestFactorial(t *testing.T) {
	require.Equal(t, 1, Factorial(0))
	require.Equal(t, 1, Factorial(1))
	require.Equal(t, 2, Factorial(2))
	require.Equal(t, 6, Factorial(3))
}
