function f = funccc(list)
b=[];
 for i = 1:length(list)-1
    if list(i+1)-list(i)>1
        b(length(b)+1)=i;
    end
 end
 f=b;
end

