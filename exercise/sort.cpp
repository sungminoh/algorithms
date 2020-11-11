#include <iostream>
#include <math.h>
#include <cstring>

using namespace std;

int N, arr[10005];

void swap(int* arr, int i, int j){
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void printArr(int arr[], int n){
    for(int i=0; i<n; ++i){
        printf("%d\t", arr[i]);
    }
    printf("\n");
}

void quickSort(int arr[], int s, int e){
    if(s >= e){
        return;
    }
    int i = s;
    int j = e;
    int p = arr[(s+e)/2];
    while(i <= j){
        while(arr[i] < p) i++;
        while(arr[j] > p) j--;
        if(i > j) break;
        swap(arr, i, j);
        i++; j--;
    }
    quickSort(arr, s, j);
    quickSort(arr, i, e);
}

void bubbleSort(int arr[], int n){
    for(int i=0; i<n; ++i){
        for(int j=n-1; j>i; --j){
            if(arr[j] < arr[j-1]){
                swap(arr, j, j-1);
            }
        }
        //printArr(arr, n);
    }
}

void selectionSort(int arr[], int n){
    int m, idx;
    for(int i=0; i<n; ++i){
        m = arr[i];
        idx = i;
        for(int j=i; j<n; ++j){
            if(arr[j] < m){
                m = arr[j];
                idx = j;
            }
        }
        swap(arr, i, idx);
        //printArr(arr, n);
    }
}

void insertionSort(int arr[], int n){
    for(int i=1; i<n; ++i){
        for(int j=i; j>0 && arr[j]<arr[j-1]; --j){
            swap(arr, j, j-1);
        }
        //printArr(arr, n);
    }
}

void mergeSort(int arr[], int s, int e){
    if(e - s <= 1){
        if(arr[s] > arr[e]){
            swap(arr, s, e);
        }
    }else{
        int p = (s+e)/2;
        mergeSort(arr, s, p);
        mergeSort(arr, p+1, e);
        int tmp[p-s+1];
        for(int i=0; i<=p-s; ++i){
            tmp[i] = arr[s+i];
        }
        int k=s;
        for(int i=0, j=p+1; i<=p-s || j<=e;){
            if(j>e || (i<=p-s && tmp[i] < arr[j])){
                arr[k++] = tmp[i++];
            }else{
                arr[k++] = arr[j++];
            }
        }
    }
}

void heapSort(int arr[], int n){
    int heap[n];
    // build heap
    for(int i=0; i<n; ++i){
        heap[i] = arr[i];
        // heapify
        for(int p=(i-1)/2, c=i; c>0; c=p, p=(p-1)/2){
            if(heap[p] > heap[c]){
                swap(heap, p, c);
            }
        }
    }
    // pop n times
    for(int i=0; i<n; ++i){
        int heapLength = n-i;
        arr[i] = heap[0];
        swap(heap, 0, heapLength - 1);
        heapLength--;
        for(int p=0; p<heapLength/2; ){
            int c1 = 2*p+1, c2 = 2*p+2;
            if(c2 < heapLength){
                if(heap[p] <= heap[c1] && heap[p] <= heap[c2]){
                    break;
                }else if(heap[c1] < heap[c2]){
                    swap(heap, p, c1);
                    p = c1;
                }else{
                    swap(heap, p, c2);
                    p = c2;
                }
            }else if(c1 < heapLength){
                if(heap[p] < heap[c1]){
                    break;
                }else{
                    swap(heap, p, c1);
                    p = c1;
                }
            }
        }
    }
}

void countSort(int arr[], int n, int base){
    // find max numberof digits
    int maxNumber = arr[0];
    for(int i=1; i<n; ++i){
        if(arr[i] > maxNumber){
            maxNumber = arr[i];
        }
    }
    int numberOfDigits = 0;
    while(maxNumber){
        numberOfDigits ++;
        maxNumber /= base;
    }
    // count
    int cnt[base];
    int tmp[n];
    int idx, divisor;
    for(int p=0; p<=numberOfDigits; ++p){
        // initialize cnt array
        memset(cnt, 0, sizeof(int)*base);
        divisor = pow(base, p);
        for(int i=0; i<n; ++i){
            idx = (arr[i] / divisor) % base;
            cnt[idx] ++;
        }
        // accumulate counts
        for(int i=1; i<base; ++i){
            cnt[i] += cnt[i-1];
        }

        // rearrange positions
        for(int i=n-1; i>=0; --i){
            idx = (arr[i] / divisor) % base;
            tmp[cnt[idx] - 1] = arr[i];
            cnt[idx] --;
        }
        memcpy(arr, tmp, sizeof(int)*n);
    }
}

void countSortGettingInput(int N, int maxNumber){
    int n;
    int arr[maxNumber+1];
    memset(arr, 0, sizeof(int) * (maxNumber+1));
    for(int i=0; i<N; ++i){
        scanf("%d", &n);
        arr[n] ++;
    }
    for(int i=0; i<= maxNumber; ++i){
        while(arr[i]--){
            printf("%d\n", i);
        }
    }
}

int main(){
    scanf(" %d", &N);
    //for(int i=0; i<N; ++i){
        //scanf(" %d", &arr[i]);
    //}

    //quickSort(arr, 0, N-1);
    //bubbleSort(arr, N);
    //selectionSort(arr, N);
    //insertionSort(arr, N);
    //mergeSort(arr, 0, N-1);
    //heapSort(arr, N);
    //countSort(arr, N, 10);
    //for(int i=0; i<N; ++i){
        //printf("%d\n", arr[i]);
        //cout << arr[i] << endl;
    //}

    countSortGettingInput(N, 10000);

    return 0;
}
