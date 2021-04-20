const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')


const handleSeclect = (selection) => {
    switch (selection) {
        case 'first':
            {
                one.classList.add('checked')
                two.classList.remove('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
            }
        case 'second':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
            }
        case 'third':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
            }
        case 'fourth':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.remove('checked')
            }
        case 'fifth':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.add('checked')
            }

    }
}