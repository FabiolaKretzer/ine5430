clear all
close all

Data=importfile('fashion-mnist_train.csv',2,inf);
input = Data(:,2:end);
target= Data(:,1);

Data=importfile('fashion-mnist_test.csv',2,inf);
input_test = Data(:,2:end);
target_test= Data(:,1);

clearvars Data;

target_string={0 'T-shirt/top';
1 'Trouser';
2 'Pullover';
3 'Dress';
4 'Coat';
5 'Sandal';
6 'Shirt';
7 'Sneaker';
8 'Bag';
9 'Ankle boot'};

figure;
colormap(gray);

perm = randperm(60000,20);
for i = 1:20
    subplot(4,5,i);
    display_array=reshape(input(perm(i),:),[28 28]);
    imshow(display_array',[]);
    xlabel(target_string{target(perm(i))+1,2});
end

% A partir deste ponto os dados j� est�o importados para o ambiente.
% Entretanto voc� tem de atentar que:
%     - as entradas e sa�das para uma rede neural no MATLAB est�o nas linhas 
% da matriz;
%     - se o problema � de classifica��o � desej�vel codificar as
% sa�das categ�ricas usando o esquema "onehot" onde cada neur�nio da camada
% de sa�da codifica uma dada categoria. 