clc
close all
picture_matrix = imread("photo_2023-03-19_06-28-55.jpg");
% I = 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
imwrite(picture_matrix, "Color.JPG");
RED_RATIO = 0.299;
GREEN_RATIO = 0.587; 
BLUE_RATIO = 0.144; 
%picture_matrix = imresize(picture_matrix ,0.05);
pSize = size(picture_matrix) ; 
gr = zeros(pSize(1), pSize(2));
for i = 1:pSize(1)
    for j= 1:pSize(2)
        gr(i , j ) =int8( 0.299 * picture_matrix(i,j,1) + 0.587*picture_matrix(i,j,2) + 0.114 * picture_matrix(i,j,3));
     
    end

end
gr = uint8(gr);

imwrite(gr , "grayscale.JPG");
m = median (gr , 'all');
gr_hc = zeros(pSize(1), pSize(2));
for i = 1:pSize(1)
    for j= 1:pSize(2)
        if (gr(i,j) < m )
            a = gr(i , j );
            gr_hc(i , j ) =  a - (a * ((50)/100 ));
        end
        if (gr(i , j > m ))
            a = gr(i , j );
            gr_hc(i , j ) =  a + (a * ((50)/100 ));
            
        end
    end
end

gr_hc = uint8(gr_hc);

imwrite(gr_hc , "grayscale_high_contrast.JPG");

gr_lc = zeros(pSize(1), pSize(2));
for i = 1:pSize(1)
    for j= 1:pSize(2)
        if (gr(i,j) <= m )
            a = gr(i , j );
            gr_lc(i , j ) =  a + (a * ((50)/100 ));
        end
        if (gr(i , j > m ))
            a = gr(i , j );
            gr_lc(i , j ) =  a - (a * ((50)/100 ));
            
        end
    end
end
gr_lc = uint8(gr_lc);
imwrite(gr_lc , "grayscale_low_contrast.JPG");


color_lc = zeros(pSize(1), pSize(2));
for i = 1:pSize(1)
    for j= 1:pSize(2)
        if (calculate_intensity(picture_matrix(i , j , :)) <= m )
            
            color_lc(i, j, 2) = picture_matrix(i, j, 2) + (calculate_intensity(picture_matrix(i , j , : ))/2);
            color_lc(i, j, 1) = picture_matrix(i, j, 1) + (calculate_intensity(picture_matrix(i , j , : ))/2); 
            color_lc(i, j, 3) = picture_matrix(i, j, 3) + (calculate_intensity(picture_matrix(i , j , : ))/2);
        end
        if (gr(i , j > m ))
           
            
            color_lc(i, j, 2) = picture_matrix(i, j, 2) - (calculate_intensity(picture_matrix(i , j , : ))/2);
            color_lc(i, j, 1) = picture_matrix(i, j, 1) - (calculate_intensity(picture_matrix(i , j , : ))/2); 
            color_lc(i, j, 3) = picture_matrix(i, j, 3) - (calculate_intensity(picture_matrix(i , j , : ))/2);
            
        end
    end
end
color_lc = uint8(color_lc);
imwrite(color_lc , "color_low.jpg");


color_hc = zeros(pSize(1), pSize(2));
for i = 1:pSize(1)
    for j= 1:pSize(2)
        if (calculate_intensity(picture_matrix(i , j , :)) <= m )
            
            color_hc(i, j, 2) = picture_matrix(i, j, 2) - (calculate_intensity(picture_matrix(i , j , : ))/2);
            color_hc(i, j, 1) = picture_matrix(i, j, 1) - (calculate_intensity(picture_matrix(i , j , : ))/2); 
            color_hc(i, j, 3) = picture_matrix(i, j, 3) - (calculate_intensity(picture_matrix(i , j , : ))/2);
        end
        if (gr(i , j > m ))
           
            
            color_hc(i, j, 2) = picture_matrix(i, j, 2) + (calculate_intensity(picture_matrix(i , j , : ))/2);
            color_hc(i, j, 1) = picture_matrix(i, j, 1) + (calculate_intensity(picture_matrix(i , j , : ))/2); 
            color_hc(i, j, 3) = picture_matrix(i, j, 3) + (calculate_intensity(picture_matrix(i , j , : ))/2);
            
        end
    end
end
color_hc = uint8(color_hc);
imwrite(color_hc , "color_high.jpg");

imwrite (gr+20  ,"manipulated_gr.jpg");


number_of_noise_cordinate = 10000 ; 
noisi_pic = gr ; 
for i = 1:number_of_noise_cordinate
    x = randi([1,pSize(1)]);
    y = randi ([1 , pSize(2)]);
    b_w  = randi([0, 1]);
    if (b_w == 1)
        noisi_pic(x,y) = int8(255);
    else
        noisi_pic(x,y) = int8(0);
    end
end
imwrite (noisi_pic  ,"salt_and_papper.jpg");




filter_size = 3 ; 
denoised_image = noisi_pic ; 
for i  = 1 : pSize(1)-filter_size
    for j = 1:pSize(2)-filter_size
        med_val = median(denoised_image(i : i + filter_size , j : j + filter_size), 'all');
        denoised_image (i , j ) = med_val;
    end
end
imwrite (denoised_image ,"denoised.jpg");

res1 = conv(gr , int8([1 0 -1 ; 2 0 -2 ; 1 0 -1]));
res2 = conv(gr , int8([1 2 1 ; 0 0 0 ; -1 -2 -1]));
imshow(res2)

function f = calculate_intensity(rgb_pixel)
    f = 0.299* rgb_pixel(1) + 0.587 * rgb_pixel(2) + 0.144 * rgb_pixel(3);
end

function f  = conv(matrix , kernel)
    kernel_size = size(kernel);
    kernel_half = idivide(int32(kernel_size(1)) , int32(2));
    pic_size = size(matrix);
    for i = kernel_half+1 : pic_size(1)-kernel_half
        for j = kernel_half+1 : pic_size(2)-kernel_half
            sum_val = 0 ;
            b = matrix(i - kernel_half : i + kernel_half , j - kernel_half : j +kernel_half);
            for x = 1 : kernel_size(1)
                for y = 1 :kernel_size(2)
                    sum_val = sum_val + kernel(x , y) * int8(b(x , y));                    
                end
            end
            matrix(i , j ) = uint8 ((sum_val));
        end
    end
    f= matrix;
end
