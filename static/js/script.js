'use strict';

$(document).ready(function () {
    $('table').on('click', '.day', function (event) {
        let target = event.target;
        $.ajax( {
            url: "/temperature/" + target.innerText + "/",

            success: function (data) {
                $('.msg').html(data.result);
            }
        })
        event.preventDefault();
    });

    let isDown = false;
    let startX;
    let scrollLeft;

    $('.my-container').on('mousedown', function (event) {
        if (event.target.localName !== 'span' && event.target.localName !== 'div') {
            isDown = true;
            startX = event.pageX - this.offsetLeft;
            scrollLeft = this.scrollLeft;
        }

    });
    $('.my-container').on('mouseleave', function (event) {
        isDown = false;
    });
    $('.my-container').on('mouseup', function (event) {
        isDown = false;
    })
    $('.my-container').on('mousemove', function (event) {
        if(!isDown) return;
        const x = event.pageX - this.offsetLeft;
        const walk = x - startX;
        this.scrollLeft = scrollLeft - walk;
    });

    const table = document.querySelector('.table');
    const cols = table.querySelectorAll('th');

    const createResizeableColumn = (col, resizer) => {
        let x = 0;
        let w = 0;

        const mouseDownHandler = event => {
            x = event.clientX;

            const styles = window.getComputedStyle(col);
            w = parseInt(styles.width, 10);

            document.addEventListener('mousemove', mouseMoveHandler);
            document.addEventListener('mouseup', mouseUpHandler);

            resizer.classList.add('resizing');
        };

        const mouseMoveHandler = event => {
            const dx = event.clientX - x;
            col.style.width = `${w + dx}px`;
        };

        const mouseUpHandler = () => {
            document.removeEventListener('mousemove', mouseMoveHandler);
            document.removeEventListener('mouseup', mouseUpHandler);

            resizer.classList.remove('resizing');
        };

        resizer.addEventListener('mousedown', mouseDownHandler);
    }

    [].forEach.call(cols, function (col) {
        const resizer = document.createElement('div');
        resizer.classList.add('resizer');

        resizer.style.height = `${table.offsetHeight}px`;

        col.appendChild(resizer);

        createResizeableColumn(col, resizer);
    });
})