subroutine Pi_rejet(N,Pi)
implicit none
real, intent(in) :: N
real, intent(out):: Pi
real :: a, b,succes,x,y
integer :: j
a=-1./2
b=1./2
succes=0.
do j=1,int(N)
x=a+(b-a)*rand()
y=a+(b-a)*rand()
if(x*x+y*y<=1./4)then
succes=succes+1.
endif
enddo
Pi=4.*succes/N
return
end subroutine
