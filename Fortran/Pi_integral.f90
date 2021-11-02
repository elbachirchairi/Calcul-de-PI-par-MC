subroutine Pi_integral(N, Pi)
    implicit none
    real*8, intent(in) :: N
    real*8, intent(out):: Pi
    real*8 :: somme,x,y
    integer :: i
    somme = 0.
    do i = 1, N
		x = rand()
		y = sqrt(1 - x*x)
		somme = somme + y    	
    end do
    Pi = 4*somme/N
    return
end subroutine Pi_integral
