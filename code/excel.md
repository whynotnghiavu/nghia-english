Sub ExtractHyperlinks()
    Dim hl As Hyperlink
    Dim ws As Worksheet
    Dim outputWs As Worksheet
    Dim row As Integer
    Dim cell As Range

    ' Tạo trang tính mới để chứa kết quả
    Set outputWs = ThisWorkbook.Worksheets.Add
    outputWs.Name = "Extracted URLs"
    outputWs.Cells(1, 1).Value = "Cell"
    outputWs.Cells(1, 2).Value = "Text"
    outputWs.Cells(1, 3).Value = "Markdown"

    row = 2

    ' Duyệt qua tất cả các trang tính
    For Each ws In ThisWorkbook.Worksheets
        ' Duyệt qua từng ô trong trang tính
        For Each cell In ws.UsedRange
            If cell.Hyperlinks.Count > 0 Then
                ' Nếu ô có siêu kết nối
                For Each hl In cell.Hyperlinks
                    outputWs.Cells(row, 1).Value = cell.Address
                    outputWs.Cells(row, 2).Value = hl.TextToDisplay
                    outputWs.Cells(row, 3).Value = "[" & hl.TextToDisplay & "](" & hl.Address & ")"
                Next hl
            Else
                ' Nếu ô không có siêu kết nối, chỉ lấy văn bản
                outputWs.Cells(row, 1).Value = cell.Address
                outputWs.Cells(row, 2).Value = cell.Value
                outputWs.Cells(row, 3).Value = "<!-- " & cell.Value & " --> " 
            End If
            row = row + 1
        Next cell
    Next ws

    MsgBox "URLs and markdown have been extracted!"
End Sub
