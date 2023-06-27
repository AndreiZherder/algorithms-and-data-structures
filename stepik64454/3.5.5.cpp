#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> cache(301, vector <int> (10001, 0));
vector<vector<bool>> has_cache(301, vector <bool> (10001, 0));

int dp(int i, int total, int s, int n, vector<int>& w, vector<int>& c) {
    if (i == n) {
        return 0;
    }
    if (has_cache[i][total]){
        return cache[i][total];
    }
    int ans = dp(i + 1, total, s, n, w, c);
    if (total + w[i] <= s) {
        ans = max(ans, dp(i + 1, total + w[i], s, n, w, c) + c[i]);
    }
    has_cache[i][total] = true;
    cache[i][total] = ans;
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t = 1;
    while (t--) {
        int s, n;
        cin >> s >> n;
        vector<int> w(n), c(n);
        for (int i = 0; i < n; i++) {
            cin >> w[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> c[i];
        }
        cout << dp(0, 0, s, n, w, c) << endl;
    }
    return 0;
}
