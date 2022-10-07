        " Leader key
        let g:mapleader = " "

        " Vem-tabline
        nmap <leader><S-tab> <Plug>vem_prev_buffer-
        nmap <leader><tab> <Plug>vem_next_buffer-
        nmap <leader>x <Plug>vem_delete_buffer-
    
        " Save and Quit
        nnoremap <silent> w :w <CR>
        nnoremap <silent> q :q <CR>

        " Delete line
        nnoremap <silent> d :d <CR>

        " Terminal
        :tnoremap <Esc> <C-\><C-n>

        " Moving line
        nnoremap <silent> <S-up> :move-2 <CR>
        nnoremap <silent> <S-down> :move+1 <CR>

        " End file
        nnoremap <silent><nowait> gh :$ <CR>
                                                          
        " Delete buffer
        nnoremap <silent> <C-d> :bw <CR>

        " Redo
        nnoremap <silent> r :redo <CR>

        " Tab new
        nnoremap <silent><nowait> nt :tabnew 

        " Tab go first
        nnoremap <silent><nowait> gft :tabfirst <CR>

        " Plug install package
        nnoremap <silent> pmi :PlugInstall

        " Plug update packages
        nnoremap <silent><nowait> pmu :PlugUpdate <CR>

        " Plug upgrade
        nnoremap <silent><nowait> pmup :PlugUpgrade <CR>

        " Plug clean
        nnoremap <silent><nowait> pmc :PlugClean <CR>

        " Open terminal
        nnoremap <silent><nowait> ot :terminal <CR>

        " Coc Explorer
        nnoremap <silent><F6> <cmd>CocCommand explorer <CR>

        " Format document
        nnoremap <silent><nowait>ff <cmd>CocCommand editor.action.formatDocument <CR> 

        " Delete line while visual mode
        vnoremap <silent>dd :'<,'>d <CR>

        " Restore Session by name
        nnoremap <silent>rs :source .config/nvim/sessions/

        " Horizontal/Vertical switch
        nnoremap <silent><nowait>wh :windo wincmd K <CR>
        nnoremap <silent><nowait>wv :windo wincmd H <CR>

        " Hide panel
        nnoremap <silent><nowait>hw :hide <CR>

        " Resise panels
        nnoremap <silent><nowait>rv :vert resize
        nnoremap <silent><nowait>rh :resize 

        " Replace
        nnoremap <silent><nowait>rw :s//g
        nnoremap <silent><nowait>rew :%s//g

        " Clear highlighting
        nnoremap <silent>ch :noh <CR>

        " Color picker
        nnoremap <silent>gc :VCoolor <CR>

        " Open Startify
        nnoremap <silent>os :Startify <CR>

        " ALE
        inoremap <C-a> :ALEDetail <CR> 
