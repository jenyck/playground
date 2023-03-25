program bubble_sort;

var massive: array [0..999] of integer;
i, j, tmp: integer;

begin
    {generates random number from [0 ; 1000] and puts it into massive}
    for i := 0 to 999 do begin
        massive[i] := Random(1001);
    end;

    {sorts massive}
    for i := 0 to 998 do begin
        {walks through massive}
        for j := 0 to 999 do begin
            {swaps variables if their order is incorrect}
            if (massive[j] < massive[j-1]) then begin
                tmp := massive[j-1];
                massive[j-1] := massive[j];
                massive[j] := tmp;
            end;
        end;
        {does it [size_of_massive] - 1 times}
    end;

    {prints all numbers from massive}
    for i := 0 to 999 do write(massive[i], ' ');
end.
