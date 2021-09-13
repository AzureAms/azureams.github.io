# Một số mẹo C++ trong phòng thi

12/09/2021  
<!-- LMAO làm cách nào cho timestamp vào blog?? -->

Có lẽ, không có kỳ thi nào đòi hỏi kỹ năng thi cao hơn các kỳ thi học sinh giỏi môn Tin học. Đã có rất nhiều thí sinh tiềm năng mất đi cơ hội đạt các giải cao hơn, hoặc tiến vào các vòng tiếp theo, chỉ vì một số lỗi rất cơ bản. Trong loạt blog này, mình sẽ tổng hợp một số lỗi thường gặp, và cách phòng tránh chúng.

## Lỗi quên "xóa debug"
Đã có rất nhiều thế hệ học sinh chuyên Tin ra khỏi phòng thi rất tự tin, vì mình đã, sau hơn 1 tiếng chỉnh đi chỉnh lại code đã AC full một bài quan trọng. Nhưng rồi lúc nhận kết quả thì bài đó... 0 điểm, đến lúc xin lại được code thì nhận ra mình... quên xóa debug.  
Xóa debug ở đây không chỉ là những lỗi ngớ ngẩn như:
```
	cout << "Ok here" << endl;
```
Mà còn có có thể hiểu rộng ra, ví dụ như một lỗi kinh điển:
```
	freopen("BAI1.INP", "r", stdin);
	//freopen("BAI1.OUT", "w", stdout);
```
(a.k.a quên `freopen`, in ra màn hình trong quá trình debug cho tiện.)  
Hay một ví dụ hài hước hơn, (thực tế 1 Amser đã bị hồi 2019):

```
	cin >> a;
	a = 4; // Để đây debug cho tiện, đỡ phải nhập đi nhập lại test mẫu nhỉ.
```

Thường thì vì mẫy lỗi này, chúng ta... mất trắng một bài, may ra thì ăn được vài trường hợp đặc biêt.  

## Phòng tránh?
Cách phòng tránh dễ nhất lỗi "quên" là... nhớ thôi! Nhưng đâu phải lúc nào cũng vậy? Có thể một bài nào đó bạn in debug chi chít, đã xóa đủ debug để test mẫu chạy trơn tru, nhưng vẫn để vài dòng `cout` lơ lửng ở mấy trường hợp còn lại. Hoặc có thể, bạn đang vội code nốt subtask cuối trong vài phút còn lại, rồi chưa kịp tìm debug hết thì giám thị đã đến tận nơi bạn tắt màn hình :(.

Vậy thì có cách nào phù phép cho các lệnh debug bay hết đi trên server chấm không?

Trong C++ có đó.

## Macros
Nếu các bạn nào đã tìm hiểu một số sản phẩm mã nguồn mở, chúng ta sẽ bắt gặp một số đoạn code kiểu như:
```C++
#ifdef _DEBUG
// Làm gì đó...
#else
// Làm việc khác.
#endif
```

`_DEBUG` ở đây chính là một "macro", một thành phần ngôn ngữ được định nghĩa bởi các câu lệnh `#define`. Trước đây có lẽ các bạn đã sử dụng các dòng `#define` để định nghĩa hằng số:
```C++
#define MOD ((int)1e9 + 7)
```
Hoặc để rút gọn một số thứ, ví dụ như:
```C++
#define ALL(x) ((x).begin()), ((x).end())
```

Ngoài công dụng thay thế một từ thành một đoạn code trước khi biên dịch, các macro trong C/C++ còn có tác dụng đánh dấu:

Ví dụ với đoạn code:

```C++
#include <iostream>
using namespace std;

int main()
{
	#ifdef DEBUG
	cout << "Hello Debug!" << endl;
	#endif
	return 0;
}
```

Chúng ta sẽ thử chạy đoạn code này và:

```

--------------------------------
Process exited after 865 milliseconds with return value 0
Press any key to continue . . .
```

Không có gì được in ra?

Nhưng ta hãy thử thêm 1 dòng `#define DEBUG` xem sao nhỉ?
```C++
#include <iostream>
using namespace std;

#define DEBUG

int main()
{
	#ifdef DEBUG
	cout << "Hello Debug!" << endl;
	#endif
	return 0;
}
```

Quan sát output, sẽ thấy:
```
Hello Debug!

--------------------------------
Process exited after 1073 milliseconds with return value 0
Press any key to continue . . .
```

Tại sao lại như vậy?  
Lệnh `#ifdef` ở đây, sẽ khiến cho trình tiền xử lý (preprocessor) kiểm tra xem thành phần ngôn ngữ đứng sau đã được định nghĩa bằng `#define` chưa, nếu đã được định nghĩa, trình xử lý này sẽ giữ nguyên đoạn mã nguồn giữa lệnh `#ifdef` này và lệnh `#endif` gần nhất. Trái lại, tất cả các đoạn mã nguồn giữa 2 lệnh trên bị loại bỏ.

Ngoài ra, ta còn có lệnh `#ifndef`, là một thứ trái ngược hoàn toàn của `#ifdef`: Chỉ giữ lại đoạn mã nguồn sau, nếu thành phần đứng sau **CHƯA ĐƯỢC ĐỊNH NGHĨA BỞI `DEFINE`**. 

Giờ thì, ta có thể viết những đoạn code như:

```C++
#define DEBUG

freopen("BAI1.INP", "r", stdin);
#ifndef DEBUG
// Trong lúc DEBUG ta muốn in ra màn hình.
freopen("BAI1.OUT", "w", stdout);
#endif

int a;
#ifdef DEBUG
// Lười nhập test mẫu, nhưng không sao.
a = 4;
#else // #else ở đây hoạt động như `else` bình thường
// Chỉ khác là nó cặp với #ifdef thay vì cặp với `if` thường.
cin >> a;
#endif

#ifdef DEBUG
cout << "Ok here." << endl;
#endif
```

Và trước giờ thi, ta chỉ cần xóa dòng `#define DEBUG` ở đầu.

## Thế nhưng quên xóa cái `#define DEBUG` ở đầu thì sao?

Thì toang. Chấm hết.

Nhưng chưa hết, ta vẫn có một cách để kích hoạt `DEBUG` mà không cần thêm `#define DEBUG` ở đầu.

Lọ mọ một chút [docs của GCC](https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html), ta thấy:

> -D name  
> Predefine name as a macro, with definition 1.  

Giờ thì ta sẽ quay lại ví dụ đầu tiên:

```C++
#include <iostream>
using namespace std;

int main()
{
	#ifdef DEBUG
	cout << "Hello Debug!" << endl;
	#endif
	return 0;
}
```

Thử biên dịch lại đoạn mã nguồn này, với câu lệnh: `g++ hello.cpp -o hello.exe -DDEBUG` xem ra sao: 


```
Hello Debug!

--------------------------------
Process exited after 690 milliseconds with return value 0
Press any key to continue . . .
```

Hay! Chúng ta đã... kích hoạt `DEBUG` mà không cần thêm dòng lệnh nào!

Một cái hay khác là, Themis - trình chấm được sử dụng phổ biến trong các kỳ thi Học sinh giỏi từ thành phố đến quốc gia, không kích hoạt `-DDEBUG`:

```
"C:\Program Files (x86)\Themis\gcc\bin\g++.exe" -std=c++14 "%NAME%%EXT%" -pipe -O2 -s -static -lm -x c++ -o"%NAME%.exe" -Wl,--stack,66060288|@WorkDir=%PATH%
```

Vậy là, trên máy tính thi, code sẽ chạy DEBUG đầy đủ, nhưng trên máy chấm, những dòng này... biến mất??

Vậy làm thế nào để thêm `-DDEBUG` khi sử dụng Dev-C++ hoặc Code::Blocks?  
Các bạn hãy vào Compiler Settings, rồi trong cái mục chỉnh "Compiler Flags", thêm `-DDEBUG` vào, là xong!

(Ở trong Dev-C++, "Compiler Settings" có thể truy cập ở `Tools -> Compiler Options`. Nhớ đánh dấu "Add the following commands when calling the compiler", và thêm options vào ô chữ ở dưới.)

![](Huong-Dan-Debug-Cpp-Img-1.png)

## Một vài lời bình luận thêm:
- Tên `DEBUG` rất phổ thông, và dễ bị đụng với các headers hệ thống. Để tránh sự đụng độ này, ta sẽ `#define` một cái tên khác, riêng biệt hơn, ví dụ như `Carano` chẳng hạn. Nếu đặt tên như vậy, nhớ thay thế `-DDEBUG` bằng `-DCarano`.
- Nếu Volkath được cử đi chấm bài và biết chuyện này, hắn ta cũng có thể thêm `-DCarano` vào Themis! Vì vậy, tuy hiếm có trường hợp thầy cô cố tình thêm macros, nhưng trong các kỳ thi quan trọng, chúng ta vẫn **nên** xóa debug khi **còn thời gian**, tránh các rủi ro do macros đem lại.

(Còn nữa)

_Các bạn hãy theo dõi loạt blog của mình, cũng như Fanpage và trang web của AzureAms để nhận thêm nhiều thông tin hữu ích như này nhé. Xin cảm ơn!_