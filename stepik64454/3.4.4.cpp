#include <iostream>
#include <vector>

#define ll long long
#define LLONG_MAX 9223372036854775807ll

using namespace std;

void calc(ll i, ll j, ll m, vector <vector <ll>> &a, vector <vector <ll>> &dp){
        if (i - 2 <= m + 1 - j) {
            while (i >= 2) {
                ll x = dp[i - 2][j - 1];
                if (dp[i - 2][j + 1] < x) {
                    x = dp[i - 2][j + 1];
                }
                if (dp[i - 1][j - 2] < x) {
                    x = dp[i - 1][j - 2];
                }
                if (dp[i + 1][j - 2] < x) {
                    x = dp[i + 1][j - 2];
                }
                if (x != LLONG_MAX) {
                    dp[i][j] = x + a[i - 2][j - 2];
                }
                i -= 1;
                j += 1;
            }
        } else {
            while (j < m + 2) {
                ll x = dp[i - 2][j - 1];
                if (dp[i - 2][j + 1] < x) {
                    x = dp[i - 2][j + 1];
                }
                if (dp[i - 1][j - 2] < x) {
                    x = dp[i - 1][j - 2];
                }
                if (dp[i + 1][j - 2] < x) {
                    x = dp[i + 1][j - 2];
                }
                if (x != LLONG_MAX) {
                    dp[i][j] = x + a[i - 2][j - 2];
                }
                i -= 1;
                j += 1;
            }
        }
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll n, m;
    cin >> n >> m;

    vector <vector <ll>> a(n, vector <ll> (m));
    for (ll i = 0; i < n; i++){
        for (ll j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    vector <vector <ll>> dp(n + 3, vector <ll> (m + 3, LLONG_MAX));
    dp[2][2] = a[0][0];

    ll row = 3;
    while (row < n + 2){
        ll i = row;
        ll j = 2;
        calc(i, j, m, a, dp);
        row += 1;
    }

    ll col = 3;
    while (col < m + 2){
        ll i = n + 1;
        ll j = col;
        calc(i, j, m, a, dp);
        col += 1;
    }


    if (dp[n + 1][m + 1] == LLONG_MAX){
        cout << "NO\n";
        return 0;
    }
    ll i = n + 1;
    ll j = m + 1;
    vector <pair <ll, ll>> ans;
    ans.emplace_back(i - 1, j - 1);

    while (i != 2 or j != 2){
        ll x = a[i - 2][j - 2];
        if (dp[i][j] == dp[i - 2][j - 1] + x) {
            i -= 2;
            j -= 1;
        }
        else if (dp[i][j] == dp[i - 1][j - 2] + x){
            i -= 1;
            j -= 2;
        }
        else if (dp[i][j] == dp[i - 2][j + 1] + x) {
            i -= 2;
            j += 1;
        } else {
            i += 1;
            j -= 2;
        }
        ans.emplace_back(i - 1, j - 1);
    }
    cout << "YES\n";
    cout << dp[n + 1][m + 1] << " " << ans.size() << "\n";
    for (auto p = ans.rbegin(); p != ans.rend(); p++){
        cout << p->first << " " << p->second << endl;
    }
    return 0;
}
