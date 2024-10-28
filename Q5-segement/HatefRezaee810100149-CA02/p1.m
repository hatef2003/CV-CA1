clc
clear
close all
[file,path]=uigetfile({'*.jpg;*.bmp;*.png;*.tif'},'Choose an image');
s=[path,file];
picture=imread(s);

picture = imresize(picture,[400 800]);
backup = picture;
a = size(size(backup));
if(a(2)==3)
picture = mygrayfun(picture);
backup = picture;
end

%%picture = mygrayfun(picture);
imshow(picture);

filtr= zeros(31,31);
for i = 1 :31
    for j = 1:31
        filtr(i,j) = 1/(31*31);
    end

end

%picture=myremovecom(picture,500);
figure
I = [1/9 1/9 1/9;1/9 1/9 1/9;1/9 1/9 1/9];
picture = imfilter(picture,filtr);
imshow(picture)
picture=mybinaryfun(picture,130);
figure
imshow(picture);
picture=myremovecom(picture,1000);
imshow(picture);
border = myremovecom(picture,7500);
figure
imshow(border);
picture= picture-border;
figure
imshow(picture);
 temp2= mysegmentation(picture);
temp = temp2{1};
temp3 =int8 (temp* 27);
figure
imshow(backup)
 Ne=temp2{2};
propied=regionprops(temp,'BoundingBox');
hold on
for n=1:size(propied,1)
    rectangle('Position',propied(n).BoundingBox,'EdgeColor','g','LineWidth',2)
end
