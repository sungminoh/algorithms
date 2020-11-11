import java.util.*;

public class Main{
    class Phone{
        int totalNoti;
        int[] noti;
        int notiIdx;
        int readIdx;

        int[] readIdxByApp;
        int[] maxIdxByApp;
        int[] notiCntByApp;

        public Phone(int n, int q){
            totalNoti = 0;
            noti = new int[q+1];
            notiIdx = 1;
            readIdx = 1;

            readIdxByApp = new int[n+1];
            maxIdxByApp = new int[n+1];
            notiCntByApp = new int[n+1];
        }

        public void add(int app){
            totalNoti++;
            noti[notiIdx] = app;
            maxIdxByApp[app] = notiIdx;
            notiCntByApp[app] += 1;
            notiIdx++;
        }

        public void read(int app){
            readIdxByApp[app] = maxIdxByApp[app];
            totalNoti -= notiCntByApp[app];
            notiCntByApp[app] = 0;
        }

        public void readHistory(int t){
            for(; readIdx<=t; readIdx++){
                int app = noti[readIdx];
                if(readIdxByApp[app] >= readIdx) continue;
                readIdxByApp[app] = readIdx;
                notiCntByApp[app]--;
                totalNoti--;
            }
        }

        public int run(int type, int param){
            switch(type){
                case 1:
                    add(param);
                    break;
                case 2:
                    read(param);
                    break;
                case 3:
                    readHistory(param);
            }
            return totalNoti;
        }
    }

    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args){
        int n = scanner.nextInt();
        int q = scanner.nextInt();

        Phone phone = new Main().new Phone(n, q);
        int[] sols = new int[q];

        int type;
        int param;
        for(int i=0; i<q; i++){
            type = scanner.nextInt();
            param = scanner.nextInt();
            sols[i] = phone.run(type, param);
        }
        for(int remainNotification : sols){
            System.out.println(remainNotification);
        }
    }
}
