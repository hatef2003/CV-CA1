function f = mybinaryfun(picture,thrsh)
for i = 1:400
    for j = 1:800
        if (picture(i,j)>thrsh)
            picture(i,j)=1;
        else 
            picture(i,j,1)=0;
        end
    end
end
f=boolean(picture);
end