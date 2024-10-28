function f = is_valid(x,y,matrix,visited)
    if (x<=400 && y<=800 && x>= 1 && y >=1)
        if (visited(x,y)==0 && matrix(x,y)==1)
            f= true;
        else
            f=false;
        end
    else
        f=false;
    end
end