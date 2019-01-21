clc;    % Clear the command window.
clear all;
close all;
workspace;  % Make sure the workspace panel is showing.
format longg;
format compact;

% Define a starting folder.
start_path = fullfile('F:\Google Drive\Microscopy\Purified Collagenase Concentration Trials 28July');
% Ask user to confirm or change.
topLevelFolder = uigetdir(start_path);
if topLevelFolder == 0
    return;
end

% Get list of all subfolders.
allSubFolders = genpath(topLevelFolder);
% Parse into a cell array.
remain = allSubFolders;
listOfFolderNames = {};
%%
% Loop true folders
while true
    [singleSubFolder, remain] = strtok(remain, ';');
    if isempty(singleSubFolder)
        break;
    end
    listOfFolderNames = [listOfFolderNames singleSubFolder];
end
numberOfFolders = length(listOfFolderNames)

% Process all image files in those folders.
counter = 1;
for k = 1 : numberOfFolders
    
    AA(k)=listOfFolderNames(k);
    
end

i=1;
for j = 1 :numberOfFolders
    
    %%change current directory (1 at a time) to run code in
    cd(AA{j})
    disp RUN_CODE
    pwd
    Q=AA{j};
    
    if exist([pwd filesep 'L.tif'], 'file')==2
        
        %% READ IN POLARISED IMAGES AND COMBINE
        A = imread('PLM1.tif');
        B = imread('PLM2.tif');
        %         figure(1);imshow(A); title('PLM1');
        %         figure(2);imshow(B); title('PLM2');
        
        Z = imadd(A,B);     %Combined PLM
        figure(3);imshow(Z); title('Combined PLM'); saveas(gcf,'PLM.tif');
        
        
        
        
        %% READ IN LIGHT IMAGES
        L = imread('L.tif'); %Light Microscopy
        figure(4); imshow(L); title('Light Microscope');
        
        
        
        %% PROCESS LIGHT IMAGES
        HSV = rgb2hsv(L);
         figure(5); imshow(HSV); title('HSV - Tissue Content');
        S=HSV(:,:,2);
         figure(6); imshow(S); title('Saturation Channel to determine tissue content');
        
        [level EM] = graythresh(L);
        BW = im2bw(S,0.2); % Select level or hard code threshold value
        invert = ~BW;
        tissue_area = sum(invert(:) == 0); %tissue content - count black pixels
        figure(7); imshow(invert); title('Tissue Content = Black')       
        
        
        %%PROCESS PLM IMAGES
        PLM_grey = rgb2gray(Z);
        figure(8); imshow(I2);
        
        
        %Adaptive method
        BW2 = imbinarize(PLM_grey, 'adaptive','Sensitivity',0.5);
        collagen_area = sum(BW2(:) == 1); %collagen content - count white pixels
        figure(9); imshow(BW2)  % collagen content = white    
        
        %Clean up stray blobs in image smaller than 80 pixels
        BW2_clean = bwareaopen(BW2, 80);
         figure(10); imshow(BW2_clean); title('Collagen content clean');
        clean_collagen_area = sum(BW2_clean(:) == 1);
        

        % CALCULATE PERCENT COLLAGEN
        content = (collagen_area)/tissue_area;
        content_clean = (clean_collagen_area)/tissue_area
        
        Collagen_content(i,1)=content_clean;
        folder=listOfFolderNames';
        
%         % SAVE CONTENT WITH LAYER INFORMATION AND INTO EXCEL
%         k1 = strfind(pwd,'Int'); % if folder name has 'Int' etc. in its
%         name, you can group into differnt columns
%         k2 = strfind(pwd,'Med');
%         k3 = strfind(pwd,'Adv');
%         % AA = cell2mat(k);
%         TF1 = isempty(k1);
%         TF2 = isempty(k2);
%         TF3 = isempty(k3);
%         if TF1 == 0
%             
%             layer(j,4)=content;
%         elseif TF2 == 0
%             
%             layer(j,5)=content;
%         elseif TF3 == 0
%             
%             layer(j,6)=content;
%         else
%             disp no
%         end
        

        %         xlswrite('F:\Google Drive\Microscopy\CollagenContent_trial_HSV_NATIVE_ADD.xlsx',layer);
        %         %  xlswrite('F:\Google Drive\Microscopy\CollagenContent_trial.xlsx',C);
        %         xlswrite('F:\Google Drive\Microscopy\CollagenContent_trial_HSV_NATIVE_ADD.xlsx',folder);
        i=i+1;
    end
end

