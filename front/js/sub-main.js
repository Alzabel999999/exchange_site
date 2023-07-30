window.onload = () => {

    document.addEventListener('click', (event) => {
        const listSelectCurrentlyFrom = document.querySelectorAll('.block-content.block-content-full.clearfix.from-currency.from-highlight');
        const listSelectCurrentlyTo = document.querySelectorAll('.block.block-rounded.block-transparent.bg-black-op.text-body-color-light.text-right.to-currency.currency-type.to-highlight');

        if (listSelectCurrentlyFrom && listSelectCurrentlyTo && listSelectCurrentlyFrom.length > 0 && listSelectCurrentlyTo.length > 0) {
            console.log('work')
            document.querySelector('.transaction-form.hidden').style = 'display: block;';
            document.querySelector('.exchange-form').style = 'display: none;';
        }
    })

}
