w_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0];

plot(w_infective(1,1:30));hold on ;
plot(w_infective(2,1:30));hold on ;
plot(w_infective(3,1:30));hold on ;
plot(w_infective(4,1:30));hold on ;
plot(w_infective(5,1:30));hold on ;
plot(w_infective(6,1:30));hold on ;
plot(w_infective(7,1:30));hold on ;
plot(w_infective(8,1:30));hold on ;
plot(w_infective(9,1:30));hold on ;
plot(w_infective(10,1:30));hold on ;
plot(w_infective(11,1:30));hold on ;

% legend('w=0','w=0.2','a=0.4','a=0.6','a=0.8', 'a=1')
legend('w=0','w=0.1','w=0.2', 'w=0.3','a=0.4', 'w=0.5','a=0.6', 'w=0.7','a=0.8','w=0.9', 'a=1')

grid on; hold off