#include <iostream>
#include <string>
/*
 * 13812345678

13812345679

第一位一定是1

后面所有位 都可能是0~9

你好！家长，您收到了优惠券，点击链接https://t.cn/xyz

10W   发送

2000 点击

140使用优惠券

你好！家长，您收到了优惠券，点击链接https://t.cn/xyznnnnnnnn

A-Z a-z 0~9

 1  最少需要多少位

2   编码和解码的程序
 * */
using namespace std;

string encode(string phone){
    string rel="";
    long long p=0;
    for(int i=1;i<phone.size();i++){
        p=p*10 + phone[i]-'0';
    }
    //cout << "debug encode "<<p<<endl;
    while(p!=0){
        if(p%62<=61 && p%62>=36){
            //cout << "debug A-Z"<<endl;
            int temp=p%62;
            temp-=36;
            rel=rel+char('A'+temp);
        }
        else if(p%62<=35 && p%62>=10){
            //cout << "debug a-z"<<endl;
            int temp=p%62;
            //cout << temp << endl;
            temp-=10;
            rel=rel+char('a'+temp);
        }
        else{
            //cout << "debug 0-9"<<endl;
            int temp=p%62;
            rel=rel+char('0'+temp);
        }
        p=p/62;
    }
    return rel;
}
string decode(string code){
    long long rel=0;
    string rels="";
    for(int i=code.size()-1;i>=0;i--){
        if(code[i]<='Z'&&code[i]>='A'){
            rel = rel*62 + 36 + code[i]-'A';
        }
        else if(code[i]<='z' && code[i]>='a'){
            rel = rel*62+10+code[i]-'a';
        }
        else {
            rel=rel*62+code[i]-'0';
        }
    }
    //cout << "debug decode "<<rel << endl;
    while(rel!=0){

        rels=char(rel%10+'0')+rels;
        rel/=10;
    }
    while(rels.size()<10){
        rels = '0' + rels;
    }
    rels = '1'+rels;
    return rels;
}
int main() {
    //int a;
    //cin >> a;
    string phone="19999999999";
    cin>>phone;
    string after = encode(phone);
    cout << after << endl;
    string before = decode(after);
    cout << before << endl;
    //cout << "Hello World!" << endl;
}