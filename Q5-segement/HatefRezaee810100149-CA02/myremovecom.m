function f = myremovecom(picture,n)
 visited=zeros(400,800);
 visited = boolean(visited);
 dx=[0,1,-1,0,1,1,-1,-1];
 dy=[1,0,0,-1,1,-1,1,-1];
 for j = 1:800
    for i =1:400
        if(visited(i,j)==0 && picture(i,j)==1)
          count = 0;
          q={[i,j]};
          comp={};
          size = 1;
          visited(i,j)=true;
           while (size~=0)
               if size == 1
                   size = 0;
                   p=q{1};
                   q={};
                   
               else
                   p = q{1};
                   q=q(2:end);
                   size=size-1;
                   
               end
               comp{end+1}=p ;
               count=count+1;
               x=p(1);
               y=p(2);
               for a = 1:8
                  newX=x+dx(a);
                  newY=y+dy(a);
                  if(is_valid(newX,newY,picture,visited))
                  q{end+1}=[newX,newY];
                  size = size +1;
                  visited(newX,newY)=true;
                  end

               end
               
           end 
           if (count<n)
               for m=1:length(comp)
                  picture(comp{m}(1),comp{m}(2))=0; 
               end
           end
        end
        
    end
 end
 f=picture;
end