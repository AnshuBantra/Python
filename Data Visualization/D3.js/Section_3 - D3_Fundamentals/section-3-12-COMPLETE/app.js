const data = [10, 20, 30, 40, 50]

const el = d3.select('ul')
  .selectAll('li')
  .data(data)
  // .join(
  //   enter => {
  //     return enter.append('li')
  //       .style('color', 'purple')
  //   },
  //   update => update.style('color', 'green'),
  //   exit => exit.remove()
  // )
  .text(d => d)

el.enter()
  .append('li')
  .text(d => d)

el.exit().remove()

console.log(el)