let forms = `
<div class = forms>
<div class="mb-3">
<label for="date" class="form-label">날짜</label>
<input type="date" class="form-control" name="date" id="date" width='50px'>
</div>
<div class="mb-3">
<label for="breakfast" class="form-label">아침</label>
<textarea class="form-control" name="breakfast"
          id="breakfast" rows="5"></textarea>
</div>
<div class="mb-3">
<label for="lunch" class="form-label">점심</label>
<textarea class="form-control" name="lunch"
          id="lunch" rows="5"></textarea>
</div>
<div class="mb-3">
<label for="dinner" class="form-label">저녁</label>
<textarea class="form-control" name="dinner"
          id="dinner" rows="5"></textarea>
</div>
</div>
<input type="button" class="btnRemove" value="삭제하기">
</div>`

$(document).ready (function () {                
    $('.btnAdd').click (function () {                                        
        $('#menuForm').append (                        
            forms
        ); // end append                            
        $('.btnRemove').on('click', function () { 
            $('.forms').remove (); 
            $(this).remove();
        });
    }); // end click                                            
}); // end ready    