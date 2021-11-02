subroutine Pi_integral(N, Pi)
implicit none
real,intent(in) :: N
real,intent(out):: Pi
real::somme,x,y
integer::i
somme=0.
do i=1,int(N)
x=rand()
y=sqrt(1-x*x)
somme=somme+y
end do
Pi=4*somme/N
return
end subroutine
