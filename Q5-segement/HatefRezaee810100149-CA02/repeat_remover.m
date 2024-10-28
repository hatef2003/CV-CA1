function f = repeat_remover(list,num)
 for i = 1:length(list)
   counts(i,1) = sum(list==list(i));
 end
 remove_it = [];
 for i = 1 : length (list)
    if(counts(i)<num)
        remove_it(length(remove_it)+1)=i;
    end
    f=remove_it;
 end
end

