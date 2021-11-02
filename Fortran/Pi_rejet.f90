subroutine Pi_rejet(N,Pi)
	implicit none
    real*8, intent(in) :: N
    real*8, intent(out):: Pi
    real*8 :: a, b, somme,succes,x,y
    integer :: i,j
    a = -1./2
    b = 1./2
    somme=0
    do i=1,20
    	succes = 0
    	do j=1,int(N)	
    		x = a + (b - a)*rand()
    		y = a + (b - a)*rand()
    		if (x*x + y*y <= 1./4) then
    			succes = succes + 1.
    		endif
    	end do
    	somme = somme + 4.*succes/N
    enddo
    Pi = somme/20.
    return
end subroutine Pi_rejet