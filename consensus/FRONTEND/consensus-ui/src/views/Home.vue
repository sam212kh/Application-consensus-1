<template>
  <section class="container-fluid">
    <div class="row row-no-padding">
      <div class="col-md-9 col-sm-9 col-xs-9">
      </div>
      <div class="col-md-3 col-sm-3 col-xs-3">
        <button class="btn btn-block btn-info">
          <i class="fa fa-plus"></i>
          Add a new School
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-12 col-sm-12 col-xs-12">
        <table class="table table-hover text-right background-white box-shadow cursor-pointer">
          <thead>
          <tr>
            <th class="text-center">
              <i class="fa fa-book color-gray"></i>
              <span class="font-weight-bold">School</span>
            </th>
            <th class="text-center">
              <i class="fa fa-calendar color-gray"></i>
              <span class="font-weight-bold">Seasons</span>
            </th>
            <th class="text-center">
              <i class="fa fa-send color-gray"></i>
              <span class="font-weight-bold">Applications</span>
            </th>
            <th class="text-center">
              <i class="fa fa-users color-gray"></i>
              <span class="font-weight-bold">Staffs</span>
            </th>
            <th class="text-center">
              <i class="fa fa-eye color-gray"></i>
              <span class="font-weight-bold">Reviewed</span>
            </th>
            <th class="text-center">
              <i class="fa fa-handshake-o color-gray"></i>
              <span class="font-weight-bold">Inrolled</span>
            </th>
          </tr>

          </thead>

          <tbody>
          <tr>
            <td class="text-left">
              <a href="#">
                School num 1
                <i class="fa fa-angle-down margin-left-10"></i>
              </a>
            </td>
            <td class="text-center">
              3
            </td>
            <td class="text-center">
              25
            </td>
            <td class="text-center">
              8
            </td>
            <td class="text-center">
              14
            </td>
            <td class="text-center">
              10
            </td>
          </tr>
          <tr>
            <td class="text-left">
              <a href="#">
                School num 2
                <i class="fa fa-angle-down margin-left-10"></i>
              </a>
            </td>
            <td class="text-center">
              5
            </td>
            <td class="text-center">
              18
            </td>
            <td class="text-center">
              8
            </td>
            <td class="text-center">
              10
            </td>
            <td class="text-center">
              10
            </td>
          </tr>
          <tr>
            <td class="text-left">
              <a href="#">
                School num 3
                <i class="fa fa-angle-down margin-left-10"></i>
              </a>
            </td>
            <td class="text-center">
              5
            </td>
            <td class="text-center">
              18
            </td>
            <td class="text-center">
              8
            </td>
            <td class="text-center">
              10
            </td>
            <td class="text-center">
              10
            </td>
          </tr>
          </tbody>

        </table>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Home"
};
</script>
