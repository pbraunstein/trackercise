import {RepHistory} from "../../models/rephistory";
export abstract class BarCharts {
    protected exerciseHistory: Array<RepHistory>;
    protected svgs: any;

    protected static ANIMATION_TIME: number = 400;  // in milliseconds
    protected static TEXT_OFFSET: number = 4;
    protected static REP_MULTIPLIER: number = 6;
    protected static VERTICAL_OFFSET: number = 170;

    protected convertJsonArrayToObjectArray(historyArray: Array<any>): Array<RepHistory> {
        let historyObjectArray: Array<RepHistory> = [];
        for (let jsonObject of historyArray) {
            historyObjectArray.push(new RepHistory(jsonObject));
        }
        return historyObjectArray;
    }

    protected splitOutSets(): void {
        let newArray: Array<RepHistory> = [];
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            for (let j = 0; j < this.exerciseHistory[i].getSets(); j++) {
                newArray.push($.extend(true, {}, this.exerciseHistory[i]));  // deep copy necessary here
            }
        }
        this.exerciseHistory = newArray;
    }

    protected setUpViz(data: any): void {
        this.exerciseHistory = this.convertJsonArrayToObjectArray(data.json().history);
                this.splitOutSets();
                let totalOffset = this.addOffsets();
                this.renderXAxis();
                this.svgs.attr('width', totalOffset)
                    .attr('height', BarCharts.VERTICAL_OFFSET * 2);
                let bars = this.svgs.selectAll('g')
                    .data(this.exerciseHistory);

                // Enter
                let barsEnter = bars.enter()
                    .append('g')
                    .attr('transform', (d: any, i: number) => 'translate(' + d.x_offset + ',' + d.y_offset + ')');
                barsEnter.append('rect')
                    .style('fill', 'blue')
                    .transition()
                    .duration(BarCharts.ANIMATION_TIME)
                    .attr('width', (d: RepHistory) => d.getWeight())
                    .attr('height', (d: RepHistory) => d.getReps() * BarCharts.REP_MULTIPLIER);
                barsEnter.append('text')
                    .attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getWeight() / 2 + ',' + -1 * BarCharts.TEXT_OFFSET + ')' + ' rotate(-45)')
                    .transition()
                    .duration(BarCharts.ANIMATION_TIME)
                    .text((d: RepHistory) => d.getReps().toString() + ',' + d.getWeight().toString());

                // Update
                bars.attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getXOffset() + ',' + d.getYOffset() + ')');
                bars.select('rect')
                    .transition()
                    .duration(BarCharts.ANIMATION_TIME)
                    .attr('width', (d: RepHistory) => d.getWeight())
                    .attr('height', (d: RepHistory) => d.getReps() * BarCharts.REP_MULTIPLIER);
                bars.select('text')
                    .attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getWeight() / 2 + ',' + -1 * BarCharts.TEXT_OFFSET + ')' + ' rotate(-45)')
                    .transition()
                    .duration(BarCharts.ANIMATION_TIME)
                    .text((d: RepHistory) => d.getReps().toString() + ',' + d.getWeight().toString());

                // Exit
                let barsExit = bars.exit();
                barsExit.select('rect')
                    .transition()
                    .duration(400)
                    .attr('height', 0);
                barsExit.transition()
                    .delay(BarCharts.ANIMATION_TIME)
                    .remove();
                barsExit.select('text')
                    .remove();
    }

    protected abstract addOffsets(): number;

    protected abstract renderXAxis(): void;
}