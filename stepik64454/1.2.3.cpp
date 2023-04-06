

#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    long long cur, a, b;
    cin >> cur >> a >> b;
    long long mod = 1791791791;
    long long pos1 = -1;
    long long pos2 = -1;
    long long mx1 = -1;
    long long mx2 = -1;
    for (int i = 0; i < n; i++){
        cur = (cur * a + b) % mod;
        if (cur > mx1){
            long long tmp = mx1;
            mx1 = cur;
            mx2 = tmp;
            tmp = pos1;
            pos1 = i;
            pos2 = tmp;
        } else if (cur > mx2) {
            mx2 = cur;
            pos2 = i;
        }
    }

    cout << pos1 + 1 << " " << pos2 + 1 << '\n';
    return 0;
}
