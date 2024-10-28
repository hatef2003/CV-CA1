function f = mygrayfun(picture)
  temp = zeros(400,800,1);
for i = 1:400
    for j = 1:800
       temp(i,j)=0.299* picture(i,j,1)+0.578*picture(i,j,2)+0.114*picture(i,j,3); 
    end
end
temp=uint8(temp);
f=temp;
end