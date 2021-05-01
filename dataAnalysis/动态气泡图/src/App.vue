<template>
  <div id="app">
    <svg id="bubble-chart" width="954" height="450" />
  </div>
</template>

<script>
import * as d3 from "d3";
import render from "d3-render";
export default {
  name: "App",
  components: {},
  data() {
    return {
      covidData: null,
      countries: null,
      colours: {
        pink: "#D8352A",
        red: "#D8352A",
        blue: "#48509E",
        green: "#02A371",
        yellow: "#F5A623",
        hyperGreen: "#19C992",
        purple: "#B1B4DA",
        orange: "#F6E7AD",
        charcoal: "#383838",
      },
    };
  },
  methods: {
    async getdata() {
      //获取新冠数据
      await this.$axios.get("data.csv").then((res) => {
        this.covidData = d3.csvParse(res.data);
      });
      //获取国家数据
      await this.$axios.get("countries.csv").then((res) => {
        this.countries = d3.csvParse(res.data);
      });
      //画图
      this.drawType();
    },

    drawType() {
      //设置svg大小
      const width = 954;
      const height = 450;
      //设置各个大洲的参数
      const continents = [
        {
          id: "AF",
          name: "Africa",
          fill: this.colours.purple,
          colour: this.colours.charcoal,
        },
        {
          id: "AS",
          name: "Asia",
          fill: this.colours.yellow,
          colour: this.colours.charcoal,
        },
        {
          id: "EU",
          name: "Europe",
          fill: this.colours.blue,
          colour: this.colours.charcoal,
        },
        {
          id: "NA",
          name: "N. America",
          fill: this.colours.pink,
        },
        {
          id: "OC",
          name: "Oceania",
          fill: this.colours.orange,
          colour: this.colours.charcoal,
        },
        {
          id: "SA",
          name: "S. America",
          fill: this.colours.green,
          colour: this.colours.charcoal,
        },
      ];

      //定义圆圈组件
      const circleComponent = ({ r, cx, cy, fill, duration }) => {
        return {
          append: "circle",
          r,
          cx,
          cy,
          fill,
          duration,
        };
      };

      //定义文字组件
      const textComponent = ({
        key,
        text,
        x = 0,
        y = 0,
        fontWeight = "bold",
        fontSize = "12px",
        textAnchor = "middle",
        fillOpacity = 1,
        colour,
        r,
        duration = 1000,
      }) => {
        return {
          append: "text",
          key,
          text,
          x,
          y,
          textAnchor,
          fontFamily: "sans-serif",
          fontWeight,
          fontSize,
          fillOpacity: { enter: fillOpacity, exit: 0 },
          fill: colour,
          duration,
          style: {
            pointerEvents: "none",
          },
        };
      };

      //对数值进行转换,比如42288变为42k
      const format = (value) => {
        const newValue = d3.format("0.2s")(value);
        if (newValue.indexOf("m") > -1) {
          return parseInt(newValue.replace("m", "")) / 1000;
        }
        return newValue;
      };

      //将各地区名称长度和数值与圆圈大小相比较，实现信息动态变化
      const labelComponent = ({ isoCode, countryName, value, r, colour }) => {
        // Don't show any text for radius under 12px
        if (r < 12) {
          return [];
        }
        //console.log(r);
        const circleWidth = r * 2;
        const nameWidth = countryName.length * 10;
        const shouldShowIso = nameWidth > circleWidth;
        const newCountryName = shouldShowIso ? isoCode : countryName;
        const shouldShowValue = r > 18;

        let nameFontSize;

        if (shouldShowValue) {
          nameFontSize = shouldShowIso ? "10px" : "12px";
        } else {
          nameFontSize = "8px";
        }

        return [
          textComponent({
            key: isoCode,
            text: newCountryName,
            fontSize: nameFontSize,
            y: shouldShowValue ? "-0.2em" : "0.3em",
            fillOpacity: 1,
            colour,
          }),
          ...(shouldShowValue
            ? [
                textComponent({
                  key: isoCode,
                  text: format(value),
                  fontSize: "10px",
                  y: shouldShowIso ? "0.9em" : "1.0em",
                  fillOpacity: 0.7,
                  colour,
                }),
              ]
            : []),
        ];
      };

      //设置气泡组件
      const bubbleComponent = ({
        name,
        id,
        value,
        r,
        x,
        y,
        fill,
        colour,
        duration = 1000,
      }) => {
        return {
          append: "g",
          key: id,
          transform: {
            enter: `translate(${x + 1},${y + 1})`,
            exit: `translate(${width / 2},${height / 2})`,
          },
          duration,
          delay: Math.random() * 300,
          children: [
            circleComponent({ key: id, r, fill, duration }),
            ...labelComponent({
              key: id,
              countryName: name,
              isoCode: id,
              value,
              r,
              colour,
              duration,
            }),
          ],
        };
      };

      const pack = (data) =>
        d3
          .pack()
          .size([width - 2, height - 2])
          .padding(2)(d3.hierarchy({ children: data }).sum((d) => d.value));

      //生成气泡图表
      const renderBubbleChart = (selection, data) => {
        const root = pack(data);
        const renderData = root.leaves().map((d) => {
          //console.log(d);
          return bubbleComponent({
            id: d.data.id,
            name: d.data.name,
            value: d.data.value,
            r: d.r,
            x: d.x,
            y: d.y,
            fill: d.data.fill,
            colour: d.data.colour,
          });
        });
        return render(selection, renderData);
      };

      const renderBubbleChartContainer = (data) => {
        return renderBubbleChart("#bubble-chart", data);
      };

      //定义新冠数据
      const covidData_result = this.covidData;
      //定义各地区数据
      const countries_result = this.countries;

      //选择数据类型为所有确诊病例数量
      const dataKey = "total_cases";
      //定义开始时间及结束时间
      const startDate = new Date("2020-01-12");
      const endDate = new Date("2020-06-02");
      //d3.map - 创建一个新的空的 map 映射
      const dates = d3
        .map(this.covidData, (d) => d.date)
        .keys()
        .map((date) => new Date(date))
        .filter((date) => date >= startDate && date <= endDate)
        .sort((a, b) => a - b);
      //各大洲全选
      const selectedContinents = ["AF", "AS", "EU", "NA", "OC", "SA"];
      //最小数值
      const minimumPopulation = 0;
      //排序
      const order = "desc";

      //转换日期格式为2020-01-01
      const getIsoDate = (date) => {
        const IsoDate = new Date(date);
        return IsoDate.toISOString().split("T")[0];
      };

      //获取最终的数据
      function getDataBy({
        dataKey,
        date,
        selectedContinents,
        order,
        minimumPopulation,
      }) {
        return (
          covidData_result
            .filter((d) => d)
            .filter((d) => d.iso_code !== "OWID_WRL")
            // Filter out countries with populations under 1 million
            .filter((d) => d.population > parseInt(minimumPopulation))
            .filter((d) => {
              return d.date === getIsoDate(date);
            })
            .filter((d) => d[dataKey])
            .filter((d) => {
              const country = countries_result.find(
                (c) => c.iso3 === d.iso_code
              );
              const continent = continents.find((c, i) => {
                if (!country) {
                  return false;
                }

                return c.id === country.continentCode;
              });

              if (!continent) {
                return false;
              }

              return selectedContinents.includes(continent.id);
            })
            .map((d) => {
              const country = countries_result.find(
                (c) => c.iso3 === d.iso_code
              );
              const continent = continents.find(
                (c) => c.id === country.continentCode
              );

              const name = country.shortName || country.name;

              return {
                name,
                id: country.iso3,
                value: d[dataKey],
                fill: continent.fill,
                colour: continent.colour || "white",
              };
            })
            .filter((d) => d.value !== "0.0")
            .sort(function (a, b) {
              const mod = order === "desc" ? -1 : 1;
              return mod * (a.value - b.value);
            })
        );
      }

      //延时执行,闭包
      for (var i = 0; i < dates.length; i++) {
        (function (i) {
          setTimeout(function () {
            const date = dates[i];
            console.log(date);
            const data = getDataBy({
              dataKey,
              date,
              selectedContinents,
              minimumPopulation,
              order,
            });
            renderBubbleChartContainer(data);
          }, 2000 * i);
        })(i);
      }
    },
  },
  mounted() {
    this.getdata();
  },
};
</script>

<style>
</style>
