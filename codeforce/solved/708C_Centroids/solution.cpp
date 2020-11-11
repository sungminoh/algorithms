#include <bits/stdc++.h>

using namespace std;

const int MAX = 400005;

int n, u, v, size[MAX], largestBranches[MAX][2], rootBranches[MAX], root;
vector<int> graph[MAX];

void dfs(int startNode, int parentNode){
    size[startNode] = 1;
    largestBranches[startNode][0] = 0;
    largestBranches[startNode][1] = 0;
    if(startNode == root || parentNode == root){
        rootBranches[startNode] = startNode;
    }else{
        rootBranches[startNode] = rootBranches[parentNode];
    }
    for(auto nextNode : graph[startNode]){
        if(nextNode == parentNode) continue;
        dfs(nextNode, startNode);
        size[startNode] += size[nextNode];
        if(size[nextNode] > size[largestBranches[startNode][0]]){
            largestBranches[startNode][1] = largestBranches[startNode][0];
            largestBranches[startNode][0] = nextNode;
        }else if(size[nextNode] > size[largestBranches[startNode][1]]){
            largestBranches[startNode][1] = nextNode;
        }
    }
}

int findRoot(){
    for(int i=1; i<=n; ++i){
        if(n - size[i] <= n/2 && size[largestBranches[i][0]] <= n/2){
            return i;
        }
    }
    printf("something goes wrong\n");
    return 0;
}

int main(){
    scanf("%d", &n);
    for(int i=1; i<n; ++i){
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    root = 1;
    dfs(root, 0);  // 0 is dummy parent node
    root = findRoot();
    dfs(root, 0);

    for(int i=1; i<=n; ++i){
        int targetBranch;
        if(rootBranches[i] == largestBranches[root][0]){
            targetBranch = largestBranches[root][1];
        }else{
            targetBranch = largestBranches[root][0];
        }
        if(n - size[rootBranches[i]] <= n/2 || n - size[i] - size[targetBranch] <= n/2){
            printf("%d ", 1);
        }else{
            printf("%d ", 0);
        }
    }
    return 0;
}
