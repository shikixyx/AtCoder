#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string S;
  cin >> S;
  int num = S.size();
  int ans = 1;
  rep(i, num) {
    if (S.at(i) == '1') {
      continue;
    } else if (S.at(i) == '+') {
      ans += 1;
    } else if (S.at(i) == '-') {
      ans -= 1;
    }
  }

  cout << ans << endl;
}
