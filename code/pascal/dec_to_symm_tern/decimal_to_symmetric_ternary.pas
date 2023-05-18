{Всерос информатика 2021-22, пробный тур муниципального этапа
Задача B. Уравновешенная система}
program decimal_to_symmetric_ternary;

uses SysUtils, StrUtils;

var is_negative: boolean;
n, i: integer;
tmp, out: string;

begin
    {gets a decimal number}
    write('Enter an integer number: ');
    readln(n);

    {checks if this number negative or positive}
    if n < 0 then begin n := abs(n); is_negative := True; end
    else is_negative := False;

    {converts the number from decimal to ternary}
    tmp := '';
    while n <> 0 do
    begin
        tmp += IntToStr(n mod 3);
        n := n div 3;
    end;
    
    {converts the number from ternary to reversed symmetric ternary}
    out := '';
    for i := 1 to length(tmp) do begin
        if tmp[i] = '0' then out += '0'
        else if tmp[i] = '1' then out += '1'
        else if tmp[i] = '2' then
        begin
            out += '$';
            tmp[i+1] := chr(ord(tmp[i+1])+1);
        end
            else
            begin
                out += '0';
                tmp[i+1] := chr(ord(tmp[i+1])+1);
            end;
    end;
    
    {reverses the number and adds a remainder if it's needed}
    out := ReverseString(out);
    if (out[1] = '$') or (out[1] = '0') then out := '1' + out;

    {makes a negative number from its absolute value if input was negative}
    if is_negative = True then
    begin
        out := StringReplace(out, '1', '_', [rfReplaceAll]);
        out := StringReplace(out, '$', '1', [rfReplaceAll]);
        out := StringReplace(out, '_', '$', [rfReplaceAll]);
    end;

    {prints the answer}
    writeln('This number in the symmetric ternary system: ', out);
end.
