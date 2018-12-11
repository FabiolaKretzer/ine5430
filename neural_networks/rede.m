
zero_matrix = zeros(60000,10);


for i = 1:60000
    
    if(target(i,1) == 0)
        zero_matrix(i,1) = 1;
    elseif(target(i,1) == 1)
        zero_matrix(i,2) = 1;
    elseif(target(i,1) == 2)
        zero_matrix(i,3) = 1;
    elseif(target(i,1) == 3)
        zero_matrix(i,4) = 1;
    elseif(target(i,1) == 4)
        zero_matrix(i,5) = 1;
    elseif(target(i,1) == 5)
        zero_matrix(i,6) = 1;
    elseif(target(i,1) == 6)
        zero_matrix(i,7) = 1;
    elseif(target(i,1) == 7)
        zero_matrix(i,8) = 1;
    elseif(target(i,1) == 8)
        zero_matrix(i,9) = 1;
    elseif(target(i,1) == 9)
        zero_matrix(i,10) = 1;
    end
end
        
TARGET = zero_matrix;        
        
zero_matrix = zeros(10000,10);
        
for i = 1:10000
    
    if(target_test(i,1) == 0)
        zero_matrix(i,1) = 1;
    elseif(target_test(i,1) == 1)
        zero_matrix(i,2) = 1;
    elseif(target_test(i,1) == 2)
        zero_matrix(i,3) = 1;
    elseif(target_test(i,1) == 3)
        zero_matrix(i,4) = 1;
    elseif(target_test(i,1) == 4)
        zero_matrix(i,5) = 1;
    elseif(target_test(i,1) == 5)
        zero_matrix(i,6) = 1;
    elseif(target_test(i,1) == 6)
        zero_matrix(i,7) = 1;
    elseif(target_test(i,1) == 7)
        zero_matrix(i,8) = 1;
    elseif(target_test(i,1) == 8)
        zero_matrix(i,9) = 1;
    elseif(target_test(i,1) == 9)
        zero_matrix(i,10) = 1;
    end
end
        
TARGET_TEST = zero_matrix;

[Data_train,PS] = mapminmax(input');
Target_train=TARGET';
Data_test=mapminmax('apply',input_test',PS);
Target_test=TARGET_TEST';

%Cria a rede neural
net=newff(Data_train,Target_train,[10],{'tansig' 'purelin'},'trainrp'); %tansig logsig
%view(net);
%net.trainFcn = 'trainrp';
%Ajusta os par?metros da rede
net.trainParam.epochs=500;   %numero maximo de epocas
net.trainParam.goal=0.001;     %erro medio quadratico desejado
net.trainParam.lr=0.1;          %taxa de aprendizado
net.trainParam.max_fail=50;     %?pocas com erro sobre validacaoo

net.divideParam.trainRatio = 0.9;
net.divideParam.valRatio = 0.1;
net.divideParam.testRatio = 0;

%Treina a rede
net=train(net,Data_train,Target_train);

Y=sim(net,Data_train);
Y_test = sim(net,Data_test);

confusion = zeros(10,60000);

for i=1:60000      %size(Data_train, 2)
	aux = max([Y(1,i), Y(2,i), Y(3,i), Y(4,i), Y(5,i), Y(6,i), Y(7,i), Y(8,i), Y(9,i), Y(10,i)]);
    for j=1:10
        if Y(j,i)== aux
            confusion(j,i)= 1;
        end
    end
end
%% 

figure;
plotconfusion(Target_train,confusion);

confusion_test = zeros(10,10000);

for i=1:10000      %size(Data_train, 2)
	aux = max([Y_test(1,i), Y_test(2,i), Y_test(3,i), Y_test(4,i), Y_test(5,i), Y_test(6,i), Y_test(7,i), Y_test(8,i), Y_test(9,i), Y_test(10,i)]);
    for j=1:10
        if Y_test(j,i)== aux
            confusion_test(j,i)= 1;
        end
    end
end

figure;
plotconfusion(Target_test,confusion_test);

