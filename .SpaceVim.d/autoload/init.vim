function! init#before() abort
  " Disable timeout before menu
  set timeoutlen=0

  " Colorscheme
  let g:ayucolor="mirage"
endfunction

function! init#after() abort
  " normal navigation in shell layer
  tnoremap <silent><C-l> <C-\><C-n>:<C-u>wincmd l<CR>
  tnoremap <silent><C-h>  <C-\><C-n>:<C-u>wincmd h<CR>
  tnoremap <silent><C-k>    <C-\><C-n>:<C-u>wincmd k<CR>
  tnoremap <silent><C-j>  <C-\><C-n>:<C-u>wincmd j<CR>
endfunction
