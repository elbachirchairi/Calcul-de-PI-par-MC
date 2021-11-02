subroutine Pi_buffon(N,D,a,Pi)
implicit none
real*8, intent(in) :: N,D,a
real*8, intent(out):: Pi
real*8 :: D1,a1,Pi_exa,succes,somme, theta,y,moy
integer :: i,j
Pi_exa = acos(-1.)
somme = 0
D1 = D/2.
a1 = a/2.
do i=1,2
succes = 0
do j=1,N
theta = Pi_exa*rand()
y = D1*rand()
if (y < a1*sin(theta)) then
succes = succes +1
end if
end	do
moy = (2.*a*N)/(D*succes)
somme = somme + moy
end do
Pi = somme/2.
end subroutine 
